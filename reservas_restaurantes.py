# Gera dados sobre reservas feitas em restaurantes.
import pandas as pd
import numpy as np
np.random.seed(42)
data = {
    "ID_Reserva": np.arange(1, 1001),
    "Número_Pessoas": np.random.randint(1, 10, 1000),
    "Data": pd.date_range(start="2023-01-01", periods=1000, freq="D"),
    "Horário": np.random.choice(["Almoço", "Jantar"], 1000),
    "Tipo_Cozinha": np.random.choice(["Italiana", "Japonesa", "Brasileira", "Francesa", "Americana"], 1000),
    "Ocasião": np.random.choice(["Negócios", "Romântico", "Família", "Amigos", "Sozinho"], 1000),
    "Preferência_Mesa": np.random.choice(["Janela", "Centro", "Terraço", "Quieto"], 1000),
    "Confirmada": np.random.choice(["Sim", "Não"], 1000)
}
df = pd.DataFrame(data)
df.to_csv("reservas_restaurantes.csv", index=False)
