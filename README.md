# Projeto-Aplicado-III
Repositório para execução do Projeto Aplicado III

1. Definição da Técnica: Filtragem Baseada em Conteúdo
A técnica selecionada para este projeto é a Filtragem Baseada em Conteúdo (Content-Based Filtering). Diferente dos sistemas de Filtragem Colaborativa, que dependem do histórico de interações de diversos usuários, esta abordagem concentra-se nas características intrínsecas dos itens (metadados).

Justificativa da Escolha:
Mitigação do Cold Start: O sistema recomenda novos filmes imediatamente, desde que possuam metadados, sem depender de avaliações de terceiros.

Explicabilidade: As sugestões são baseadas em atributos claros como elenco, diretor e gênero.

Metodologia Matemática: Similaridade de Cosseno
Para comparar os filmes, as representações textuais são convertidas em vetores numéricos. A Similaridade de Cosseno mede o ângulo entre esses vetores para determinar o nível de afinidade. O cálculo resulta em um valor entre 0 e 1, onde 1 indica que os filmes são muito parecidos e 0 indica que não possuem relação.

2. Treinamento do Modelo (Prova de Conceito)
O treinamento consiste na construção da Matriz de Similaridade via script movie-train.py:

Etapa A: Vetorização (Bag of Words)
Utilizou-se o CountVectorizer para transformar a coluna "soup" em uma matriz de contagem de tokens. Cada termo único (como o nome de um ator ou um gênero) torna-se uma dimensão no espaço vetorial do modelo.

Etapa B: Processamento e Filtragem
O modelo processou 3.127 títulos, garantindo densidade de dados para que as conexões entre os filmes fossem estatisticamente relevantes.

Etapa C: Validação dos Resultados
A prova de conceito apresentou resultados coerentes nos testes realizados no terminal:

Entrada: Avatar | Sugestão: Guardians of the Galaxy | Motivo: Similaridade em Gênero e Keywords (Espaço).

Entrada: Pirates of the Caribbean | Sugestão: Dead Man's Chest | Motivo: Identidade de Elenco, Diretor e Gênero.

Esse formato ficou melhor para você? Se precisar de mais algum ajuste ou quiser que eu escreva a conclusão final do trabalho, é só avisar.
