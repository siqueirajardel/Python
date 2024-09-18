# Gera dados sobre transações bancárias de clientes.
import pandas as pd
import numpy as np
np.random.seed(42)
data = {
    "ID": np.arange(1, 1001),
    "Valor_Transação": np.random.randint(50, 5000, 1000),
    "Tipo_Transação": np.random.choice(["Depósito", "Retirada", "Pagamento", "Transferência"], 1000),
    "Canal_Transação": np.random.choice(["Online", "ATM", "Agência", "App Móvel"], 1000),
    "Data": pd.date_range(start="2023-01-01", periods=1000, freq="D"),
    "Conta_Origem": np.random.randint(100000, 999999, 1000),
    "Conta_Destino": np.random.randint(100000, 999999, 1000),
    "Status": np.random.choice(["Concluído", "Pendente", "Cancelado"], 1000),
    "Moeda": np.random.choice(["USD", "EUR", "BRL", "JPY", "GBP"], 1000)
}
df = pd.DataFrame(data)
df.to_csv("transacoes_bancarias.csv", index=False)
