import pandas as pd

data = pd.read_csv('PAD_03_PD.csv', sep=';')

counts = data.groupby('Country').size()
print(counts)

