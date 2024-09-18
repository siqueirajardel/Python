import pandas as pd
import numpy as np

# Configurando a semente para reprodutibilidade
np.random.seed(42)

# Gerando nomes de usuários de forma simulada
usuarios = ["Usuario" + str(i) for i in range(1, 1001)]

# Gerando 1000 dados aleatórios
data = {
    "ID_Usuário": np.arange(1, 1001),
    "Nome_Usuário": usuarios,
    "Horas_TV": np.random.rand(1000) * 4,
    "Horas_Streaming": np.random.rand(1000) * 4,
    "Horas_Rádio": np.random.rand(1000) * 2,
    "Horas_Jogos": np.random.rand(1000) * 3,
    "Artigos_Lidos": np.random.randint(0, 20, 1000),
    "Podcasts_Ouvidos": np.random.randint(0, 10, 1000),
    "Mídia_Favorita": np.random.choice(["TV", "Streaming", "Rádio", "Jogos", "Leitura", "Podcasts"], 1000),
    "Assinaturas": np.random.randint(0, 5, 1000)
}

df = pd.DataFrame(data)

# Salvando os dados em um arquivo CSV
df.to_csv("consumo_midia_usuarios.csv", index=False)

print("Arquivo 'consumo_midia_usuarios.csv' criado com sucesso.")
