import pandas as pd
import numpy as np
import pydataset as pds
import matplotlib.pyplot as plt

print('*****************************************')
print('EXERCICIO 1')
dfPaises = pd.read_csv('paises.csv', delimiter=';')
df = dfPaises[dfPaises['Region'].str.contains('OCEANIA')]
print(df)

df1 = dfPaises.groupby(by='Region').size()
print(df1)

print('*****************************************')
print('EXERCICIO 2')
print(dfPaises['Population'].max())

print('*****************************************')
print('EXERCICIO 3')
g2 = dfPaises.groupby('Region')
print(g2['Literacy (%)'].mean())

print('*****************************************')
print('EXERCICIO 4')
dfPaises['Coastline(coast/area ratio)' == 0].to_csv('noCoast.csv')


print('*****************************************')
print('EXERCICIO 5')
def death(value):
    if value < 9:
        return 'Balanced'
    else:
        return 'Urgent'

print(dfPaises['Deathrate'].apply(death))