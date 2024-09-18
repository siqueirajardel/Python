import pandas as pd
import numpy as np

# Configurando a semente para reprodutibilidade
np.random.seed(42)

# Gerando nomes de usuários de forma simulada
usuarios = ["Usuário" + str(i) for i in range(1, 1001)]

# Gerando 1000 dados aleatórios
data = {
    "ID": np.arange(1, 1001),
    "Nome_Usuário": usuarios,
    "Posts": np.random.randint(0, 50, 1000),
    "Likes": np.random.randint(0, 500, 1000),
    "Comentários": np.random.randint(0, 300, 1000),
    "Compartilhamentos": np.random.randint(0, 100, 1000),
    "Seguidores_Ganhos": np.random.randint(-50, 150, 1000),
    "Seguindo": np.random.randint(0, 500, 1000),
    "Data": pd.date_range(start="2023-01-01", periods=1000, freq="D"),
    "Plataforma": np.random.choice(["Facebook", "Twitter", "Instagram", "TikTok", "LinkedIn"], 1000)
}

df = pd.DataFrame(data)

# Salvando os dados em um arquivo CSV
df.to_csv("atividades_redes_sociais_com_id_usuarios.csv", index=False)

print("Arquivo 'atividades_redes_sociais_com_id_usuarios.csv' criado com sucesso.")
