import numpy as np
"""
arr.ndim
arr.shape
"""
a1 = np.array([[1,2,3], [10, 20]])
print(a1.ndim)

a2 = np.array([[1,2,3], [10, 20, 30]])
print(a2.ndim)

a3 = np.array([1,2,3])
b3 = np.array([[1,2,3], [11,12,13]])
c3 = np.array([[[1,2,3], [2,3,4]], [ [11,12,13], [10,11,12] ] ])
print(a3)
print(a3.shape)
print(b3)
print(b3.shape)
print(c3)
print(c3.shape)


