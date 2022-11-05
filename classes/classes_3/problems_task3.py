import pandas as pd

data = pd.read_csv('PAD_03_PD.csv', sep=';')
data['owned_goods'] = data.apply(lambda row: row['owns_car'] + row['owns_TV'] + row['owns_house'] + row['owns_Phone'],
                                 axis=1)

mean = data.groupby('gender')['owned_goods'].mean().round(2)
print(mean)