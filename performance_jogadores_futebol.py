import pandas as pd
import numpy as np

# Configurando a semente para reprodutibilidade
np.random.seed(42)

# Gerando nomes fictícios de jogadores
nomes_jogadores = ["Jogador " + str(i) for i in range(1, 1001)]

# Gerando 1000 dados aleatórios
data = {
    "ID": np.arange(1, 1001),
    "Nome_Jogador": nomes_jogadores,
    "Gols": np.random.randint(0, 30, 1000),
    "Assistências": np.random.randint(0, 20, 1000),
    "Cartões_Amarelos": np.random.randint(0, 10, 1000),
    "Cartões_Vermelhos": np.random.randint(0, 3, 1000),
    "Jogos_Disputados": np.random.randint(0, 38, 1000),
    "Minutos_Jogados": np.random.randint(90, 3420, 1000),
    "Chutes_Ao_Gol": np.random.randint(0, 100, 1000),
    "Defesas_Goleiro": np.random.randint(0, 150, 1000)  # Apenas para jogadores que são goleiros
}

df = pd.DataFrame(data)

# Salvando os dados em um arquivo CSV
df.to_csv("performance_jogadores_futebol_com_nomes.csv", index=False)

print("Arquivo 'performance_jogadores_futebol_com_nomes.csv' criado com sucesso.")
