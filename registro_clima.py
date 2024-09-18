# Gera dados sobre condições climáticas diárias.
import pandas as pd
import numpy as np
np.random.seed(42)
data = {
    "ID": np.arange(1, 1001),
    "Temperatura_Max": np.random.randint(15, 35, 1000),
    "Temperatura_Min": np.random.randint(5, 20, 1000),
    "Precipitação_mm": np.random.rand(1000) * 100,
    "Umidade_%": np.random.randint(30, 100, 1000),
    "Velocidade_Vento_km/h": np.random.rand(1000) * 50,
    "Direção_Vento": np.random.choice(["Norte", "Sul", "Leste", "Oeste"], 1000),
    "Cobertura_Nuvem_%": np.random.randint(0, 100, 1000),
    "Pressão_atm": np.random.randint(970, 1030, 1000)
}
df = pd.DataFrame(data)
df.to_csv("registro_clima.csv", index=False)
