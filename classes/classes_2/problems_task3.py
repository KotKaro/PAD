import numpy as np
import pandas as pd
import datetime

data = pd.read_csv('Seattle2014.csv')

data['DATE'] = pd.to_datetime(data['DATE'], format='%Y%m%d')
data['PRCP'] = data['PRCP'].values/254.0


print("Number days without rain:", np.sum(data['PRCP'] == 0))
print("Number days with rain:", np.sum(data['PRCP'] > 0))
print("Days with more than 0.5 inches:", np.sum(data['PRCP'] > 0.5))
print("Rainy days with 0.2 inches:", np.sum(data['PRCP'] == 0.2))

summerPrcp = data.where(data['PRCP'] > 0) \
    .where((datetime.datetime(2014, 6, 21) < data['DATE']) & (datetime.datetime(2014, 9, 21) > data['DATE']))\
    ['PRCP']

nonSummerPrcp = data.where(data['PRCP'] > 0)\
    .where((datetime.datetime(2014, 6, 21) > data['DATE']) | (datetime.datetime(2014, 9, 21) < data['DATE']))\
    ['PRCP']

print("Median precip on rainy days in 2014 (inches):", data.where(data['PRCP'] > 0).where(data['DATE'].dt.year == 2014)['PRCP'].median())
print("Median precip on summer days in 2014 (inches):", summerPrcp.median())
print("Maximum precip on summer days in 2014 (inches):", summerPrcp.max())
print("Median precip on non-summer rainy days (inches):", nonSummerPrcp.median())