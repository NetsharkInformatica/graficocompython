import pandas as pd
import plotly.express as px

tabela = pd.read_csv('relacoesVenda.csv')

#print(tabela)

grafico = px.bar(tabela,
                 x='Vendas',y='Pais',orientation='h',color='Pais',text='Vendas',
                 range_x=[0,tabela['Vendas'].max()],
                 animation_frame='Ano',
                 animation_group='Pais')
                 


# grafico = px.bar(tabela,
#                  x='Vendas',
#                  y='Pais',
#                  orientation='h',
#                  color='Pais', 
#                  text_auto='.2f',  # Mostrar valores com 2 casas decimais
#                  range_x=[0, tabela['Vendas'].max()],
#                  animation_frame='Ano',
#                  animation_group='Pais'
#                  )

grafico.write_html('corrida de vendas por pais')