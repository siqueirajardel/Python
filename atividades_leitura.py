import pandas as pd
import numpy as np

# Configurando a semente para reprodutibilidade
np.random.seed(42)

# Gerando nomes de leitores de forma simulada
leitores = ["Leitor" + str(i) for i in range(1, 1001)]

# Expandindo a lista de gêneros literários
generos = ["Ficção", "Não-ficção", "Suspense", "Educativo", "Biografia",
           "Fantasia", "Ciência", "História", "Romance", "Terror", "Autoajuda",
           "Aventura", "Poesia", "Manga", "Graphic Novel", "Filosofia", "Humor",
           "Infantil", "Jovem Adulto", "Mistério"]

# Gerando 1000 dados aleatórios
data = {
    "ID_Leitor": np.arange(1, 1001),
    "Nome_Leitor": leitores,
    "Livros_Lidos": np.random.randint(0, 50, 1001),
    "Páginas_Diárias": np.random.randint(10, 100, 1001),
    "Gênero_Favorito": np.random.choice(generos, 1001),
    "Tempo_Leitura_min": np.random.randint(0, 120, 1001),
    "Ebook_vs_Papel": np.random.choice(["Ebook", "Papel"], 1001),
    "Clube_Leitura": np.random.choice(["Sim", "Não"], 1001),
    "Análise_Livro": np.random.randint(1, 5, 1001)
}

df = pd.DataFrame(data)

# Salvando os dados em um arquivo CSV
df.to_csv("atividades_leitura_leitores_generos_expandidos.csv", index=False)

print("Arquivo 'atividades_leitura_leitores_generos_expandidos.csv' criado com sucesso.")
