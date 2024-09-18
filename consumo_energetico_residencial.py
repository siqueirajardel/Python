# Gera dados sobre o consumo energético em residências.
import pandas as pd
import numpy as np
np.random.seed(42)
data = {
    "ID": np.arange(1, 1001),
    "Consumo_kWh": np.random.randint(100, 1000, 1000),
    "Custo_Energia": np.random.rand(1000) * 100,
    "Temperatura_Média": np.random.randint(10, 35, 1000),
    "Número_Pessoas": np.random.randint(1, 6, 1000),
    "Área_m²": np.random.randint(50, 500, 1000),
    "Tipo_Residência": np.random.choice(["Apartamento", "Casa", "Condomínio"], 1000),
    "Região": np.random.choice(["Norte", "Sul", "Leste", "Oeste", "Centro-Oeste"], 1000)
}
df = pd.DataFrame(data)
df.to_csv("consumo_energetico_residencial.csv", index=False)
