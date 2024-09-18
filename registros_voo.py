# Gera dados sobre voos de uma companhia aérea.
import pandas as pd
import numpy as np
np.random.seed(42)
data = {
    "ID": np.arange(1, 1001),
    "Número_Voo": np.random.randint(100, 9999, 1000),
    "Destino": np.random.choice(["Nova York", "Londres", "Paris", "Tóquio", "São Paulo"], 1000),
    "Duração_Voo_hrs": np.random.rand(1000) * 12,
    "Atraso_Min": np.random.randint(0, 240, 1000),
    "Companhia_Aérea": np.random.choice(["Delta", "United", "LATAM", "British Airways", "Air France"], 1000),
    "Classe": np.random.choice(["Econômica", "Executiva", "Primeira Classe"], 1000),
    "Taxa_Ocupação_%": np.random.randint(50, 100, 1000),
    "Data": pd.date_range(start="2023-01-01", periods=1000, freq="D")
}
df = pd.DataFrame(data)
df.to_csv("registros_voo.csv", index=False)
