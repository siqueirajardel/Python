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
    "Passos_Diários": np.random.randint(1000, 20000, 1000),
    "Calorias_Consumidas": np.random.randint(1200, 3500, 1000),
    "Horas_Sono": np.random.rand(1000) * 8,
    "Peso_kg": np.random.rand(1000) * 50 + 50,  # Peso variando entre 50kg e 100kg
    "Água_Litros": np.random.rand(1000) * 3,
    "Exercícios_Semana": np.random.randint(0, 7, 1000),
    "Meditação_Min": np.random.randint(0, 60, 1000),
    "Satisfação_%": np.random.randint(0, 100, 1000)
}

df = pd.DataFrame(data)

# Salvando os dados em um arquivo CSV
df.to_csv("saude_bemestar_usuarios.csv", index=False)

print("Arquivo 'saude_bemestar_usuarios.csv' criado com sucesso.")
