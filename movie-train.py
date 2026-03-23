import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Carregar os dados que o seu movie-clean.py gerou
df = pd.read_csv(r'C:\Users\pedro\OneDrive\Área de Trabalho\4º Semestre\Projeto Aplicado III\movies_ready_to_train.csv')

# 2. Vetorização (Transforma a 'soup' em números para o algoritmo entender)
count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df['soup'].fillna(''))

# 3. Cálculo da Similaridade de Cosseno (A lógica de recomendação)
cosine_sim = cosine_similarity(count_matrix, count_matrix)

def recomendar(titulo):
    try:
        # Pega o índice do filme pelo título
        idx = df[df['title'] == titulo].index[0]
        
        # Ordena os filmes por similaridade
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        # Pega os 5 filmes mais parecidos
        top_indices = [i[0] for i in sim_scores[1:6]]
        
        print(f"\n🎬 Recomendações para '{titulo}':")
        for i in top_indices:
            print(f"- {df['title'].iloc[i]}")
    except:
        print(f"\n❌ Filme '{titulo}' não encontrado.")

# --- TESTE O SISTEMA ---
recomendar("Avatar")
recomendar("Pirates of the Caribbean: At World's End")