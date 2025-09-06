# Importa as bibliotecas necessárias
import pandas as pd  # Para manipulação de dados em DataFrames
from sklearn.linear_model import LinearRegression  # Para criar o modelo de regressão linear
import plotly.express as px  # Para criar gráficos interativos

# Carrega os dados do arquivo CSV para um DataFrame do pandas
# O arquivo 'dados.csv' deve conter as colunas 'Mes' e 'Vendas'
tabela = pd.read_csv("dados.csv")

# Converte a coluna 'Mes' para o tipo numérico
# Isso é importante para que a regressão linear possa processar esses dados
tabela["Mes"] = pd.to_numeric(tabela["Mes"])

# Define a variável dependente (y) e as variáveis independentes (x)
# 'Vendas' é a variável que queremos prever (y)
# 'Mes' é a variável que usaremos para fazer a previsão (x)
y = tabela["Vendas"]
lista_dados = ["Mes"]
x = tabela[lista_dados]

# Cria e treina o modelo de regressão linear
# O modelo aprenderá a relação entre 'Mes' e 'Vendas'
modelo = LinearRegression()
modelo.fit(x, y)

# Cria um DataFrame com os meses para os quais queremos fazer previsões
# Aqui, estamos prevendo as vendas para os meses 52, 53 e 55
mes_prever = pd.DataFrame({"Mes": [52, 53, 55]})

# Realiza as previsões usando o modelo treinado
previsao = modelo.predict(mes_prever)

# Cria um DataFrame para armazenar as previsões
# Inclui o 'Mes' e as 'Vendas' previstas, e uma coluna 'Tipo' para identificar como 'Previsão'
tabela_previsao = pd.DataFrame({"Mes": mes_prever["Mes"], "Vendas": previsao})
tabela_previsao["Tipo"] = "Previsão"

# Adiciona uma coluna 'Tipo' ao DataFrame original para identificar os dados como 'Historico'
tabela["Tipo"] = "Historico"

# Concatena os dados históricos e os dados de previsão em um único DataFrame
# Isso é feito para que ambos possam ser plotados no mesmo gráfico
tabela_grafico = pd.concat([tabela, tabela_previsao])

# Cria um gráfico de linha interativo usando Plotly Express
# - x='Mes': Eixo horizontal representa os meses
# - y='Vendas': Eixo vertical representa as vendas
# - color='Tipo': Diferencia os dados históricos das previsões por cor
# - title: Título do gráfico
# - markers=True: Adiciona marcadores aos pontos de dados para maior clareza
grafico = px.line(tabela_grafico, x="Mes", y="Vendas", color="Tipo", title="Vendas x Mês com Previsão", markers=True)

# Salva o gráfico gerado em um arquivo HTML
# Este arquivo pode ser aberto em qualquer navegador web para visualizar o gráfico interativo
grafico.write_html("grafico_previsao.html")


# Exibe o gráfico interativo

grafico.show()