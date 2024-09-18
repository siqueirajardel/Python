# Gera dados sobre produção agrícola de uma fazenda.
import pandas as pd
import numpy as np
np.random.seed(42)
data = {
    "ID": np.arange(1, 1001),
    "Produto": np.random.choice(["Milho", "Soja", "Trigo", "Arroz", "Café"], 1000),
    "Quantidade_Produzida_ton": np.random.rand(1000) * 100,
    "Área_Cultivada_ha": np.random.rand(1000) * 50,
    "Custo_Produção_$": np.random.rand(1000) * 10000,
    "Preço_Venda_$": np.random.rand(1000) * 15000,
    "Lucro_$": np.random.rand(1000) * 5000,
    "Safra": np.random.choice(["2022/2023", "2023/2024"], 1000)
}
df = pd.DataFrame(data)
df.to_csv("producao_agricola.csv", index=False)
