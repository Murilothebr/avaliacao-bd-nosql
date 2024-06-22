import numpy as np
import datetime as dt
import pandas as pd

dados = pd.read_csv('vendas.csv')

#region Pergunta 1

office_supplies_df = dados[dados['Categoria'] == 'Office Supplies']

vendas_por_cidade = office_supplies_df.groupby('Cidade')['Valor_Venda'].sum()

cidade_maior_venda = vendas_por_cidade.idxmax()
valor_maior_venda = vendas_por_cidade.max()

print(f"A cidade com o maior faturamento na categoria 'Office Supplies' é {cidade_maior_venda} com vendas de {valor_maior_venda:.2f}.")

#endregion


#region Pergunta 2

## Pergunta de Negócio 2 (nível easy):
### Qual o total de vendas segmentado por dia (data do pedido)?



#endregion