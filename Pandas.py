import matplotlib
import pandas as pd
from pandas.io.sql import execute

exemplo1 = [10, 20, 30, 40, 50];
series1 = pd.Series(data=exemplo1)

# print(series1)

exemplo2 = { 'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E': 500}

series2 = pd.Series(data = exemplo2)

# print(series2)

import pandas as pd
url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'
dfs = pd.read_html(url)

print(type(dfs))
print(len(dfs))

df_bancos = dfs[0]

print(df_bancos.shape)

print(df_bancos.dtypes)

print(df_bancos.head(5))


print('---------------------------------')

df_selic = pd.read_json('https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json')

print(df_selic)
print(df_selic.info())

df_selic.drop_duplicates(keep='last', inplace=True)

print(df_selic)

from datetime import date
from datetime import datetime as dt

data_extracao = date.today()

df_selic['data_extracao'] = data_extracao
df_selic['responsavel'] = "Felipe"

print(df_selic.info())
print('-----------------------')
print(df_selic.head())
print('--------------------')
print(df_selic.loc[0])
print('--------------------')
print(df_selic.loc[[0, 20, 30]])
print('--------------------')

teste = df_selic['valor'] < 0.01
print(teste)


import matplotlib.pyplot as plt

import random

dados1 =  random.sample(range(100), k=20)
dados2 = random.sample(range(100), k=20)

print(plt.plot(dados1,dados2))

import pandas as pd

dados = {

    'Produto': ['A', 'B', 'C'],

    'qtde_vendida': [33, 50, 45]

}

df = pd.DataFrame(dados)

df.plot(x='Produto', y='qtde_vendida', kind='bar')

df.plot(x='Produto', y='qtde_vendida', kind='pie')

df.plot(x='Produto', y='qtde_vendida', kind='line')

matplotlib.pyplot.show()

import seaborn as sns

import matplotlib.pyplot as plt

sns.set(style='whitegrid')

df_tips = sns.load_dataset('tips')

fig, ax = plt.subplots(1, 3, figsize=(15, 5))

sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[0])
matplotlib.pyplot.show()

sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[1], estimator=sum)
matplotlib.pyplot.show()

sns.barplot(data=df_tips, x='sex', y='total_bill', ax=ax[2], estimator=len)
matplotlib.pyplot.show()

import seaborn as sns

import matplotlib.pyplot as plt

sns.set(style='whitegrid')



df = sns.load_dataset('tips')

plt.figure(figsize=(8, 5))

sns.barplot(x='time', y='total_bill', data=df, estimator=sum, ci=None, palette='Set2')

plt.xlabel('Período (Time)')

plt.ylabel('Total de Gastos')

plt.title('Total de Gastos por Período (Almoço ou Jantar)')

plt.show()

plt.figure(figsize=(8, 5))

sns.barplot(x='time', y='total_bill', data=df)#, #estimator=sum, ci=None, palette=“Set2”)

plt.xlabel('Período (Time)')

plt.ylabel('Média de Gastos')

plt.title('Média de Gastos por Período (Almoço ou Jantar)')

plt.show()

# Crie um gráfico de barras com o Seaborn para mostrar a média de gorjetas por período

plt.figure(figsize=(8, 5))

sns.barplot(x='time', y='total_bill', data=df, palette='Set3')

plt.xlabel('Período (Time)')

plt.ylabel('Média da Gorjeta')

plt.title('Média da Gorjeta por Período (Almoço ou Jantar)')

plt.show()

import sqlite3

from pandas.io.sql import execute

conn = sqlite3.connect(("funcionarios.db"))

cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    cargo TEXT,
    salario REAL
    )
''')

novo_funcionario = (3, "Lucia", "Analista", 5000.00)
cursor.execute('INSERT INTO funcionarios VALUES (?,?,?,?)', novo_funcionario)
conn.commit()

cursor.execute('SELECT * FROM funcionarios')
funcionarios = cursor.fetchall()
print('Funcionarios Cadastrados: ')
for funcionario in funcionarios:
    print(funcionario)