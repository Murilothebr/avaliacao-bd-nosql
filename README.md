Avaliaçao 2 de banco de dados NoSql

Análise de Vendas
# Importação das bibliotecas
import numpy as np
import pandas as pd
import datetime as dt
Fazendo o carregamento do arquivo e as verificações iniciais dos dados.
# Carrega o dataset
dados = pd.read_csv('vendas.csv')
# analisando o shape do arquivo
dados.shape
# analisando uma amostra dos dados
dados.head()
# Colunas do conjunto de dados
dados.info()
# Resumo estatístico da coluna valor de venda
dados['Valor_Venda'].describe()
# Verificando se há registros duplicados. No caso não existem
dados[dados.duplicated()]
# Verificando quantos valores ausentes existem em cada coluna. No caso nenhum
dados.isnull().sum()
## Pergunta de Negócio 1 (nível easy):

### Qual cidade onde foi feito o maior faturamento com vendas de produtos da categoria 'Office Supplies'?

## Pergunta de Negócio 2 (nível easy):

### Qual o total de vendas segmentado por dia (data do pedido)?


## Pergunta de Negócio 3 (nível easy):

### Qual o total de vendas por estado?

## Pergunta de Negócio 4 (Nível easy):

### Quais são as 10 cidades onde a loja teve maior faturamento em vendas?

## Pergunta de Negócio 5 (nível médio):

### Qual cliente da cidade de Los Angeles geral mais faturamento (gastou mais dinheiro na loja)?

## Pergunta de Negócio 6 (Nível médio):

### Qual o total de vendas por Segmento e por ano?

## Pergunta de Negócio 7 (Nível Rambo):

## Os gestores da empresa estão pensando em considerar oferecer descontos conforme o valor dos pedidos. Basicamente, pedidos inferiores a 1000 teriam desconto de 10% e acima deste valor um desconto de 15%. Desta forma, considerando os dados que temos, eles gostariam de fazer uma simulação, para ter ideia de quantos pedidos receberiam os desconto de 15%.

### Quantas vendas receberiam desconto de 10% e de 15% seguindo esta regra?

## Pergunta de Negócio 8 (Nível Verdão):
### Considerando que a empresa decida oferecer os descontos (de 10% ou 15%) citados na questão anterior. Qual seria a queda percentual no faturamento da empresa?


