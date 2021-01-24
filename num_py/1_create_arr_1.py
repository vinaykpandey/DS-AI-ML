import numpy as np

a1 = np.array([1, 2, 3])  # 1-d array
print(a1)

a2 = np.array([[1, 2, 3], [10, 20, 30]])  # 2-d array
print(a2)

a3 = np.array([[1, 2, 3], [10, 20]])  # 1-d array element as list (because its not matrix)
# array([list([1, 2, 3]), list([10, 20])], dtype=object)
print(a3)

a3 = np.array([[1, 2, 3], "Hello"])
print(a3)

# data types: int, object, U21
a4 = np.array([[1, 2, 3], [10, 'b', 'c']])
print(a4)

a5 = np.array([[1, 2, 3], [10, 7.0, 4]])
print(a5)
