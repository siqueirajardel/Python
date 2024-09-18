import pandas as pd
import numpy as np

# Configurando a semente para reprodutibilidade
np.random.seed(42)

# Gerando nomes de alunos de forma simulada
nomes = ["Aluno " + str(i) for i in range(1, 1001)]

# Gerando turmas de forma aleatória
turmas = ["Turma A", "Turma B", "Turma C", "Turma D", "Turma E"]
turmas_aleatorias = np.random.choice(turmas, 1000)

# Gerando 1000 dados aleatórios
data = {
    "ID": np.arange(1, 1001),
    "Nome": nomes,
    "Turma": turmas_aleatorias,
    "Matemática": np.random.randint(0, 100, 1000),
    "Ciências": np.random.randint(0, 100, 1000),
    "História": np.random.randint(0, 100, 1000),
    "Literatura": np.random.randint(0, 100, 1000),
    "Esportes": np.random.randint(0, 100, 1000),
    "Artes": np.random.randint(0, 100, 1000),
    "Música": np.random.randint(0, 100, 1000),
    "Tecnologia": np.random.randint(0, 100, 1000)
}

df = pd.DataFrame(data)

# Salvando os dados em um arquivo CSV
df.to_csv("desempenho_estudantes_completo.csv", index=False)

print("Arquivo 'desempenho_estudantes_completo.csv' criado com sucesso.")
