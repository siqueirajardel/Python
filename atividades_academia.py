import pandas as pd
import numpy as np

# Configurando a semente para reprodutibilidade
np.random.seed(42)

# Gerando nomes de clientes de forma simulada
clientes = ["Cliente " + str(i).zfill(2) for i in range(1, 1001)]

# Gerando 1000 dados aleatórios
data = {
    "ID_Cliente": clientes,
    "Horas_Cardio": np.random.rand(1000) * 2,
    "Horas_Força": np.random.rand(1000) * 2,
    "Kilometragem_Corrida": np.random.rand(1000) * 10,
    "Levantamento_Peso": np.random.randint(20, 200, 1000),
    "Dias_Academia_Semana": np.random.randint(1, 7, 1000),
    "Proteina_Consumida": np.random.randint(50, 250, 1000),
    "Água_Litros": np.random.rand(1000) * 3,
    "Horas_Sono": np.random.rand(1000) * 8
}

df = pd.DataFrame(data)

# Salvando os dados em um arquivo CSV
df.to_csv("atividade_academia_clientes.csv", index=False)

print("Arquivo 'atividade_academia_clientes.csv' criado com sucesso.")
