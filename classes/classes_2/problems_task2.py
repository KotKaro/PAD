import numpy as np
import pandas as pd

data = np.genfromtxt('Zadanie_2.csv', delimiter=';')
eigenvalues, vectors = np.linalg.eig(data)
print(eigenvalues)
print('-------')
print(vectors)

print('inverted')
print(np.linalg.inv(data))

