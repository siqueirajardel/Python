# Gera dados sobre o desempenho de vários aplicativos móveis.
import pandas as pd
import numpy as np
np.random.seed(42)
data = {
    "ID": np.arange(1, 1001),
    "Downloads": np.random.randint(1000, 50000, 1000),
    "Avaliação_Média": np.random.rand(1000) * 5,
    "Comentários_Pos": np.random.randint(0, 1000, 1000),
    "Comentários_Neg": np.random.randint(0, 500, 1000),
    "Renda_Publicidade": np.random.randint(100, 10000, 1000),
    "In_App_Purchases_Média": np.random.rand(1000) * 50,
    "Usuários_Ativos": np.random.randint(100, 10000, 1000),
    "Churn_Rate_%": np.random.rand(1000) * 100
}
df = pd.DataFrame(data)
df.to_csv("desempenho_apps_móveis.csv", index=False)
