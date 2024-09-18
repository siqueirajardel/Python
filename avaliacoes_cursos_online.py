import pandas as pd
import numpy as np

# Configurando a semente para reprodutibilidade
np.random.seed(42)

# Expandindo a lista de categorias
categorias = [
    "Desenvolvimento de Software", "Design Gráfico", "Marketing Digital",
    "Data Science", "Finanças", "Empreendedorismo", "Saúde Mental",
    "Nutrição", "Exercícios Físicos", "Música", "Artes", "Línguas",
    "História", "Literatura", "Filosofia", "Astronomia", "Ecologia",
    "Psicologia", "Educação", "Culinária"
]

# Gerando nomes de cursos fictícios
nomes_cursos = ["Curso de " + categoria for categoria in categorias]
# Para garantir variedade, vamos replicar e misturar os nomes
nomes_cursos_repetidos = np.random.choice(nomes_cursos, 1000)

# Gerando 1000 dados aleatórios
data = {
    "ID_Curso": np.arange(1, 1001),
    "Nome_Curso": nomes_cursos_repetidos,
    "Inscritos": np.random.randint(100, 10000, 1000),
    "Avaliação": np.random.rand(1000) * 5,
    "Conclusão_%": np.random.randint(0, 100, 1000),
    "Carga_Horária_hrs": np.random.randint(1, 50, 1000),
    "Categoria": np.random.choice(categorias, 1000),
    "Preço_$": np.random.randint(0, 200, 1000),
    "Certificado": np.random.choice(["Sim", "Não"], 1000)
}

df = pd.DataFrame(data)

# Salvando os dados em um arquivo CSV
df.to_csv("avaliacao_cursos_online_expandido.csv", index=False)

print("Arquivo 'avaliacao_cursos_online_expandido.csv' criado com sucesso.")
