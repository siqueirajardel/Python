# Gera dados sobre o progresso de projetos em uma organização.
import pandas as pd
import numpy as np
np.random.seed(42)
data = {
    "ID_Projeto": np.arange(1, 1001),
    "Nome_Projeto": ["Projeto " + str(i) for i in range(1, 1001)],
    "Horas_Trabalhadas": np.random.randint(10, 2000, 1000),
    "Custo_$": np.random.randint(1000, 50000, 1000),
    "Status": np.random.choice(["Planejamento", "Em Execução", "Concluído", "Cancelado"], 1000),
    "Prioridade": np.random.choice(["Alta", "Média", "Baixa"], 1000),
    "Data_Início": pd.date_range(start="2021-01-01", periods=1000, freq="W"),
    "Data_Fim": pd.date_range(start="2023-01-01", periods=1000, freq="W")
}
df = pd.DataFrame(data)
df.to_csv("gestao_projetos.csv", index=False)
