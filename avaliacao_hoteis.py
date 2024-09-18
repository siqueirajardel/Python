import pandas as pd
import numpy as np

# Configurando a semente para reprodutibilidade
np.random.seed(42)

# Gerando nomes fictícios de hotéis
nomes_hoteis = ["Hotel Sol Nascente", "Hotel Vista do Vale", "Hotel Águas Claras", 
                "Hotel Pedra Grande", "Hotel Céu Azul", "Hotel Flores do Campo",
                "Hotel Mar Aberto", "Hotel Serra Bela", "Hotel Praia Serena", 
                "Hotel Campo Verde"]
# Repetindo a lista para ter 1000 entradas, garantindo variedade e repetição
nomes_hoteis_repetidos = np.random.choice(nomes_hoteis, 1000)

# Gerando 1000 dados aleatórios
data = {
    "ID_Hotel": np.arange(1, 1001),
    "Nome_Hotel": nomes_hoteis_repetidos,
    "Avaliação": np.random.randint(1, 5, 1000),
    "Noites_Estadia": np.random.randint(1, 14, 1000),
    "Tipo_Quarto": np.random.choice(["Standard", "Deluxe", "Suite"], 1000),
    "Café_da_Manha": np.random.choice(["Sim", "Não"], 1000),
    "Piscina": np.random.choice(["Sim", "Não"], 1000),
    "Limpeza": np.random.randint(1, 5, 1000),
    "Conforto": np.random.randint(1, 5, 1000),
    "Localização": np.random.randint(1, 5, 1000)
}

df = pd.DataFrame(data)

# Salvando os dados em um arquivo CSV
df.to_csv("avaliacao_hoteis_com_nomes.csv", index=False)

print("Arquivo 'avaliacao_hoteis_com_nomes.csv' criado com sucesso.")


