import pandas as pd
import numpy as np
import pydataset as pds
import matplotlib.pyplot as plt

dfrio = pd.read_csv('rio.csv', delimiter=',')
df1 = dfrio.head()
#print(df1)

df2 = dfrio.loc[(dfrio['weight']) >= 150]

df3 = df2['sport'].unique()
print(df3)

