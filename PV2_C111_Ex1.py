import pandas as pd
import numpy as np
import pydataset as pds
import matplotlib.pyplot as plt

df = pd.read_csv('rio.csv', delimiter=',')
df1 = df.head()

dfmale = df[df['sex'].str.contains('male')]
dffemale = df[df['sex'].str.contains('female')]

dfmale1 = len(dfmale)
dffemale1 = len(dffemale)

print('Masculino:', dfmale1)
print('Feminino:', dffemale1)

plt.bar(['Masculino', 'Feminino'], [dfmale1, dffemale1], color = 'red')
plt.show()