import pandas as pd
import numpy as np
import pydataset as pds
import matplotlib.pyplot as plt

df = pd.read_csv('rio.csv', delimiter=',')
df1 = df.head()
#print(df1) - height

df2 = df.loc[(df['sport']) == 'volleyball']
df3 = df2.loc[(df2['sex']) == 'female']

df4 = df3['height'].mean()

print('A Altura média para atletas do volleyball feminino é:', df4)