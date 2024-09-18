# Gera dados sobre vendas de automóveis em uma concessionária.
import pandas as pd
import numpy as np
np.random.seed(42)
data = {
    "ID": np.arange(1, 1001),
    "Preço": np.random.randint(20000, 100000, 1000),
    "Ano": np.random.randint(2000, 2023, 1000),
    "Quilometragem": np.random.randint(0, 200000, 1000),
    "Marca": np.random.choice(["Toyota", "Ford", "Chevrolet", "Volkswagen", "Honda"], 1000),
    "Modelo": np.random.choice(["Sedan", "SUV", "Hatchback", "Caminhão", "Van"], 1000),
    "Cor": np.random.choice(["Preto", "Branco", "Vermelho", "Azul", "Cinza"], 1000),
    "Combustível": np.random.choice(["Gasolina", "Diesel", "Elétrico", "Híbrido"], 1000),
    "Estado": np.random.choice(["Novo", "Usado"], 1000)
}
df = pd.DataFrame(data)
df.to_csv("vendas_automoveis.csv", index=False)
