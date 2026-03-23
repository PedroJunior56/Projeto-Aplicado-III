# Projeto-Aplicado-III
Repositório para execução do Projeto Aplicado III

Projeto de Sistema de Recomendação de Filmes - Projeto Aplicado III
Este projeto apresenta o desenvolvimento de um sistema de recomendação baseado em conteúdo, focado na análise de metadados para sugerir títulos similares aos usuários. O trabalho foi estruturado em etapas de Extração, Transformação e Carga (ETL) e Modelagem Estatística.

1. Bibliotecas Python Utilizadas

Pandas: Utilizada para a manipulação e análise de estruturas de dados. 

Scikit-Learn (Sklearn): Utilizamos especificamente: CountVectorizer Para converter a sopa de metadados textuais em vetores numéricos (Tokenização), e Cosine Similarity: Para realizar o cálculo matemático da distância entre os vetores e identificar os filmes mais próximos entre si.

Ast: Biblioteca nativa do Python utilizada para converter as strings das colunas (que originalmente vêm em formato de lista de dicionários do dataset cru) em objetos Python reais, permitindo extrair os nomes dos atores e diretores.

2. Processo de ETL e Preparação de Dados
O tratamento dos dados foi realizado em duas etapas principais para garantir a integridade das informações:

Primeira Etapa: Filtragem e Redução que gerou o Arquivo movies_projeto.csv
A base de dados original passou por uma triagem para focar em dados de alta qualidade:

Seleção de Atributos: Mantivemos Id, Titulo , Gênero, Palavras-Chaves, Elenco , Média de voto, Quantidade de voto

Filtro de Relevância: Aplicou-se um filtro de popularidade (percentil 35%), resultando em um dataset de 3.127 títulos, garantindo metadados mais densos.

Segunda Etapa: Limpeza e Normalização (Arquivo movies_ready_to_train.csv)
Utilizou-se o script movie-clean.py para preparar o texto:

Tratamento de Caracteres: Remoção de acentos e correção de codificação Unicode.

Case Folding: Conversão de todo o conteúdo para letras minúsculas.

Processamento do Elenco: Junção de nomes e sobrenomes para evitar que o algoritmo trate partes de um nome como palavras separadas.

Metadata Soup: Criação de uma coluna única combinando os principais atributos para servir como base de conhecimento do filme.

3. Definição da Técnica e Modelagem
A técnica escolhida foi a Filtragem Baseada em Conteúdo (Content-Based Filtering). Esta abordagem utiliza as características dos itens para gerar recomendações, sendo eficiente para recomendar itens sem depender de um histórico prévio de outros usuários.

Metodologia Matemática: Similaridade de Cosseno
Para quantificar a semelhança, o sistema utiliza a Similaridade de Cosseno. Os textos são convertidos em vetores e o algoritmo calcula o ângulo entre eles. O resultado varia de 0 a 1, onde valores próximos a 1 indicam forte correlação.

4. Treinamento do Modelo e Prova de Conceito
O treinamento foi realizado através do script movie-train.py:

Etapa A: Vetorização (Bag of Words)
O CountVectorizer transformou as palavras em uma matriz de contagem, permitindo que o modelo identifique padrões e repetições de atores e temas.

Etapa B: Execução e Validação
A prova de conceito validou a eficácia do modelo:

Exemplo: Ao inserir o filme Avatar, o modelo recomendou títulos como Guardians of the Galaxy, identificando correlação em Gênero e Temática Espacial.

Exemplo: Ao inserir Pirates of the Caribbean, o modelo recomendou as sequências da franquia, validando a identificação do elenco e gênero de aventura.
