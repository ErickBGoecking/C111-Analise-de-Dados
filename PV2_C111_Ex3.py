import pandas as pd
import numpy as np
import pydataset as pds
import matplotlib.pyplot as plt

dfrio = pd.read_csv('rio.csv', delimiter=',')
#print(dfrio.head())

x = dfrio.loc[dfrio['gold'].idxmax()]

print('Nome:', x['name'])
print('Nacionalidade:', x['nationality'])
print('Esporte:', x['sport'])

