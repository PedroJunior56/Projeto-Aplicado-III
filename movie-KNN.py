import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors

# 1. Carregar os dados
# Certifique-se de manter o caminho correto
df = pd.read_csv(r'C:\Users\pedro\OneDrive\Área de Trabalho\4º Semestre\Projeto Aplicado III\movies_ready_to_train.csv')

# 2. Vetorização (Mantém-se a mesma para manter a base de comparação)
count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df['soup'].fillna(''))

# 3. Configuração do Modelo KNN
# n_neighbors=6 (5 recomendações + o próprio filme)
# metric='cosine' para manter a lógica de similaridade que você usava antes
knn = NearestNeighbors(n_neighbors=6, metric='cosine')
knn.fit(count_matrix)

def recomendar(titulo):
    try:
        # Pega o índice do filme pelo título
        idx = df[df['title'] == titulo].index[0]
        
        # Consulta o modelo KNN
        # distances retorna a distância (similaridade) e indices os IDs dos filmes
        distances, indices = knn.kneighbors(count_matrix[idx])
        
        # indices[0] traz os vizinhos mais próximos. 
        # O primeiro elemento é o próprio filme (distância 0), então pegamos de [1:]
        top_indices = indices[0][1:]
        
        print(f"\n🎬 Recomendações (KNN) para '{titulo}':")
        for i in top_indices:
            print(f"- {df['title'].iloc[i]}")
            
    except IndexError:
        print(f"\nFilme '{titulo}' não encontrado.")
    except Exception as e:
        print(f"\nErro ao processar: {e}")

# TESTE DO SISTEMA
recomendar("Avengers: Age of Ultron")
recomendar("A Christmas Carol")