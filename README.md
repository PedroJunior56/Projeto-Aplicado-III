# Projeto-Aplicado-III
Repositório para execução do Projeto Aplicado III

Este projeto apresenta o desenvolvimento de um sistema de recomendação baseado em conteúdo, focado na análise de metadados para sugerir títulos similares aos usuários. O trabalho foi estruturado em etapas de Extração, Transformação e Carga (ETL) e Modelagem Estatística.

1. Processo de ETL e Preparação de Dados
O tratamento dos dados foi realizado em duas etapas principais para garantir a integridade das informações antes do treinamento do modelo:

Primeira Etapa: Filtragem e Redução (Arquivo movies_projeto.csv)
A base de dados original passou por uma triagem para focar em dados de alta qualidade:

Seleção de Atributos: Foram mantidas apenas as colunas essenciais: ID, Título, Gênero, Elenco (Cast), Palavras-chave (Keywords), Média de voto e Quantidade de voto.

Filtro de Relevância: Aplicou-se um filtro de popularidade (percentil 35%), resultando em um dataset de 3.127 títulos. Isso garantiu que o modelo trabalhasse com filmes que possuem metadados completos.

Segunda Etapa: Limpeza e Normalização (Arquivo movies_ready_to_train.csv)
Utilizou-se o script movie-clean.py para preparar o texto para o algoritmo:

Tratamento de Caracteres: Remoção de acentos e correção de erros de codificação Unicode.

Case Folding: Conversão de todo o conteúdo para letras minúsculas.

Processamento do Elenco: Junção de nomes e sobrenomes (ex: johnny depp para johnnydepp). Essa técnica evita que o algoritmo trate nomes comuns como palavras separadas, aumentando a precisão da identificação do ator.

Metadata Soup: Criação de uma coluna única combinando Elenco, Gêneros e Keywords, servindo como a base de conhecimento do filme.

2. Definição da Técnica: Filtragem Baseada em Conteúdo
A técnica escolhida foi a Filtragem Baseada em Conteúdo (Content-Based Filtering). Esta abordagem utiliza as características dos itens para gerar recomendações, sendo eficiente para mitigar o problema de Cold Start (início a frio), onde o sistema consegue recomendar itens novos sem depender de um histórico prévio de avaliações de usuários.

Metodologia Matemática: Similaridade de Cosseno
Para quantificar a semelhança entre os filmes, o sistema utiliza a Similaridade de Cosseno. Os textos da Metadata Soup são convertidos em vetores numéricos e o algoritmo calcula o cosseno do ângulo entre eles. O resultado varia de 0 a 1, onde valores próximos a 1 indicam forte correlação entre os metadados dos filmes comparados.

3. Treinamento do Modelo e Prova de Conceito
O treinamento do modelo foi realizado através do script movie-train.py e consiste na geração da Matriz de Similaridade:

Etapa A: Vetorização (Bag of Words)
Utilizou-se o CountVectorizer para transformar as palavras em uma matriz de contagem. Cada termo único no dataset torna-se uma dimensão no espaço vetorial, permitindo que o modelo identifique padrões e repetições de atores, diretores e temas.

Etapa B: Execução e Validação
A prova de conceito validou a eficácia do modelo através de testes reais com o dataset processado:

Exemplo 1: Ao inserir o filme Avatar, o modelo recomendou Guardians of the Galaxy e Alien, identificando a forte correlação nos gêneros de Ficção Científica e temas espaciais.

Exemplo 2: Ao inserir Pirates of the Caribbean: At World's End, o modelo recomendou as sequências diretas da franquia, validando a identificação precisa do elenco (johnnydepp) e do gênero de aventura.

Este fluxo garante um sistema de recomendação robusto, onde a qualidade da saída é diretamente proporcional ao rigor aplicado na limpeza e tratamento inicial dos dados.
