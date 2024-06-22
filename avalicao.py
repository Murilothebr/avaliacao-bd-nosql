import numpy as np
import datetime as dt
import pandas as pd
import locale

# region Formatar Valor das moedas para não ficar zoado o output
locale.setlocale(locale.LC_ALL, 'us_US.UTF-8')
def formatar_moeda(valor):
    return locale.currency(valor, grouping=True)
#endregion

#region Pergunta 1

# dados = pd.read_csv('vendas.csv')

# office_supplies_df = dados[dados['Categoria'] == 'Office Supplies']

# vendas_por_cidade = office_supplies_df.groupby('Cidade')['Valor_Venda'].sum()

# cidade_maior_venda = vendas_por_cidade.idxmax()
# valor_maior_venda = formatar_moeda(vendas_por_cidade.max())

# print(f"A cidade com o maior faturamento na categoria 'Office Supplies' é {cidade_maior_venda} com vendas de {valor_maior_venda}.")

#endregion

#region Pergunta 2

## Pergunta de Negócio 2 (nível easy):
### Qual o total de vendas segmentado por dia (data do pedido)?

# dados = pd.read_csv('vendas.csv')

# dados['Data_Pedido'] = pd.to_datetime(dados['Data_Pedido'], dayfirst=True)

# vendas_por_dia = dados.groupby('Data_Pedido')['Valor_Venda'].sum()

# ordenadas = vendas_por_dia.sort_values(ascending=False)

# print(vendas_por_dia.apply(formatar_moeda))

#endregion

#region Pergunta 3

##Pergunta de Negócio 3 (nível easy):

###Qual o total de vendas por estado?

# dados = pd.read_csv('vendas.csv')

# dados_estado = dados.groupby('Estado')['Valor_Venda'].sum()
# ordenadas = dados_estado.sort_values(ascending=False)

# print(ordenadas.apply(formatar_moeda))

#endregion

#region Pergunta 4

## Pergunta de Negócio 4 (Nível easy):

### Quais são as 10 cidades onde a loja teve maior faturamento em vendas?

# dados = pd.read_csv('vendas.csv')

# dados_cidade = dados.groupby('Cidade')['Valor_Venda'].sum()
# dados_cidade_valor = dados_cidade.sort_values(ascending=False)

# print(dados_cidade_valor.head(10).apply(formatar_moeda))

#endregion

#region Pergunta 5

## Pergunta de Negócio 5 (nível médio):
### Qual cliente da cidade de Los Angeles geral mais faturamento (gastou mais dinheiro na loja)?

# dados = pd.read_csv('vendas.csv')

# dados_cidade = dados[dados['Cidade'] == 'Los Angeles']
# dados_top_clientes = dados.groupby('ID_Cliente')['Valor_Venda'].sum()

# print(dados_top_clientes.idxmax())

#endregion

#region Pergunta 6

## Pergunta de Negócio 6 (Nível médio):
### Qual o total de vendas por Segmento e por ano?

# dados = pd.read_csv('vendas.csv')

# dados['Data_Pedido'] = pd.to_datetime(dados['Data_Pedido'], dayfirst=True)

# dados['Ano'] = dados['Data_Pedido'].dt.year

# dados_segmento_data = dados.groupby([ 'Segmento', 'Ano' ])['Valor_Venda'].sum()

# print(dados_segmento_data.apply(formatar_moeda))

#endregion

#region Pergunta 7

## Pergunta de Negócio 7 (Nível Rambo):
# Os gestores da empresa estão pensando em considerar oferecer descontos conforme o valor dos pedidos. Basicamente, pedidos inferiores a 1000 teriam desconto de 10% e acima deste valor um desconto de 15%. Desta forma, considerando os dados que temos, eles gostariam de fazer uma simulação, para ter ideia de quantos pedidos receberiam os desconto de 15%.
### Quantas vendas receberiam desconto de 10% e de 15% seguindo esta regra?

# dados = pd.read_csv('vendas.csv')

# quantidade_10 = dados.where(dados['Valor_Venda'] < 1000).dropna()
# quantidade_15 = dados.where(dados['Valor_Venda'] > 1000).dropna()

# count_quantidade_10 = quantidade_10['Valor_Venda'].count()
# count_quantidade_15 = quantidade_15['Valor_Venda'].count()

# print(f'quantidade com 10% = {count_quantidade_10}')
# print(f'quantidade com 15% = {count_quantidade_15}')

#endregion

#region Pergunta 8
## Pergunta de Negócio 8 (Nível Verdão):
### Considerando que a empresa decida oferecer os descontos (de 10% ou 15%) citados na questão anterior. Qual seria a queda percentual no faturamento da empresa?

dados = pd.read_csv('vendas.csv')

quantidade_10 = dados.where(dados['Valor_Venda'] < 1000).dropna()
quantidade_15 = dados.where(dados['Valor_Venda'] > 1000).dropna()



#endregion
