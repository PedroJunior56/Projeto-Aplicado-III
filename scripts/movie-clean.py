import pandas as pd
import re
import unicodedata
import ast

def limpeza_flexivel(texto):
    if pd.isna(texto) or texto == "" or not isinstance(texto, str):
        return ""
    
    # 1. Normaliza Unicode logo de cara (resolve o \u00e5 do Skarsgard e acentos)
    texto = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode('ascii')
    
    # 2. Caso o texto ainda seja JSON/Lista (com chaves ou colchetes)
    if '[' in texto or '{' in texto:
        try:
            # Tenta converter para lista real
            dados = ast.literal_eval(texto.replace('""', '"'))
            if isinstance(dados, list):
                nomes = []
                for item in dados[:3]:
                    n = str(item.get('name', ''))
                    # Gruda nome e sobrenome (Johnny Depp -> johnnydepp)
                    n = re.sub(r'[^a-zA-Z]', '', n).lower()
                    if n: nomes.append(n)
                return " ".join(nomes)
        except:
            # Se falhar, tenta pegar via Regex o que estiver em "name"
            nomes_brutos = re.findall(r'"name":\s*"([^"]+)"', texto.replace('""', '"'))
            if not nomes_brutos:
                nomes_brutos = re.findall(r"'name':\s*'([^']+)'", texto)
            
            res = [re.sub(r'[^a-zA-Z]', '', n).lower() for n in nomes_brutos[:3]]
            if res: return " ".join(res)

    # 3. Caso o texto já seja simples (como o seu exemplo: Johnny Depp Orlando Bloom...)
    # Apenas remove caracteres especiais, mantém espaços entre palavras e põe em minúsculo
    texto_limpo = re.sub(r'[^a-zA-Z\s]', '', texto).lower()
    # Opcional: Você pode tentar "grudar" nomes aqui se souber que são sempre pares, 
    # mas o mais seguro para texto simples é manter as palavras separadas.
    return " ".join(texto_limpo.split())

# --- EXECUÇÃO ---
path_projeto = r'C:\Users\pedro\OneDrive\Área de Trabalho\4º Semestre\Projeto Aplicado III\movies_projeto.csv'
df = pd.read_csv(path_projeto)

print("Iniciando limpeza inteligente (JSON ou Texto)...")

for col in ['genres', 'keywords', 'cast']:
    print(f"Limpando: {col}")
    df[col] = df[col].apply(limpeza_flexivel)

# Criando a 'Sopa' garantindo que os termos não fiquem grudados entre as colunas
df['soup'] = df['keywords'].fillna('') + ' ' + df['cast'].fillna('') + ' ' + df['genres'].fillna('')

# Salvando
path_final = r'C:\Users\pedro\OneDrive\Área de Trabalho\4º Semestre\Projeto Aplicado III\movies_ready_to_train.csv'
df.to_csv(path_final, index=False, encoding='utf-8')


print(f"Título: {df['title'].iloc[1]}")
print(f"Cast: {df['cast'].iloc[1]}")
print(f"Soup: {df['soup'].iloc[1]}")