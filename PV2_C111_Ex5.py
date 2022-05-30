import pandas as pd
import numpy as np
import pydataset as pds
import matplotlib.pyplot as plt

dfrio = pd.read_csv('rio.csv', delimiter=',')

df1 = dfrio[['id', 'nationality']]
df1 = df1.groupby('nationality').count()
df1 = df1.nlargest(3, 'id')
print(df1)

plt.pie(df1['id'].values, labels=df1.index.values, colors=['red', 'yellow', 'black'])
# plt.legend()
plt.show()
