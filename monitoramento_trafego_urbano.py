# Gera dados sobre o monitoramento de tráfego urbano em diferentes locais.
import pandas as pd
import numpy as np
np.random.seed(42)
data = {
    "ID_Interseção": np.arange(1, 1001),
    "Veículos_Hora": np.random.randint(100, 5000, 1000),
    "Acidentes_Mês": np.random.randint(0, 10, 1000),
    "Tempo_Semáforo_s": np.random.randint(30, 180, 1000),
    "Faixas": np.random.randint(1, 8, 1000),
    "Tipo_Veículo_Dominante": np.random.choice(["Carro", "Moto", "Ônibus", "Caminhão", "Bicicleta"], 1000),
    "Zona": np.random.choice(["Residencial", "Comercial", "Industrial", "Mista"], 1000),
    "Dia_Semana": np.random.choice(["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"], 1000)
}
df = pd.DataFrame(data)
df.to_csv("monitoramento_trafego_urbano.csv", index=False)
