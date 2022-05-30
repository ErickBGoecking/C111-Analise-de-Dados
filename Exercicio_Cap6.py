import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#EXERCÍCIO 1
dfSpace = pd.read_csv('space.csv', delimiter=';')

dfUSA = dfSpace[dfSpace['Location'].str.contains('USA')]
USA = dfUSA['Company Name'].unique()
qtdUSA = len(USA)

dfChina = dfSpace[dfSpace['Location'].str.contains('China')]
CHINA = dfChina['Company Name'].unique()
qtdChina = len(CHINA)

plt.bar(['CHINA', 'USA'], [qtdChina, qtdUSA], color = 'red')
plt.show()

#EXERCÍCIO 2
dfPaises = pd.read_csv('paises.csv', delimiter=';')

df_NA = dfPaises[dfPaises['Region'].str.contains('NORTHERN AMERICA')]

plt.plot(df_NA['Deathrate'], 'r-', label='Deathrate')
plt.plot(df_NA['Birthrate'], 'b--', label='Birthrate')

plt.legend()
plt.show()