# Gera dados sobre tráfego em um website.
import pandas as pd
import numpy as np
np.random.seed(42)
data = {
    "ID": np.arange(1, 1001),
    "Visitas": np.random.randint(100, 10000, 1000),
    "Tempo_Médio_Sessão_min": np.random.rand(1000) * 30,
    "Taxa_Rejeição_%": np.random.rand(1000) * 100,
    "Conversões": np.random.randint(0, 500, 1000),
    "Origem_Tráfego": np.random.choice(["Direto", "Email", "Redes Sociais", "Referência", "Orgânico"], 1000),
    "Páginas_Visitadas": np.random.randint(1, 20, 1000),
    "Dispositivo": np.random.choice(["Desktop", "Mobile", "Tablet"], 1000)
}
df = pd.DataFrame(data)
df.to_csv("trafego_web.csv", index=False)
