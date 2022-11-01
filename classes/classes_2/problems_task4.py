import numpy as np

A = [0, 3, 2, 5]
B = [0, 3, 1, 4]

aArray = np.array(A)
bArray = np.array(B)

# 1 - sum
arraysSum = aArray + bArray
print(arraysSum)

# 2 - subtraction
arraysSub = bArray - aArray
print(arraysSub)

# 3 - a multiplied by 4
aMulByFour = aArray * 4
print(aMulByFour)

# 4 - scalar product
product = np.dot(aArray, bArray)
print(product)

# 5 - len of B
print(bArray.shape)