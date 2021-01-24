import numpy as np

a1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype="float32")

print(a1[1, 1])
a1[1, 1] = np.nan
print(a1)
print("*"*40)
a2 = np.zeros((2, 4))
print(a2)

print("*"*40)
a2 = np.ones((2, 4))
print(a2)
"""
0 OR 1  is fn to fill in nd array
"""

print("*"*40)
a2 = np.full((2, 4), 11)
print(a2)

"""
identity matrix  (mxm)
principal diagonal is 1 and other values are 0
"""
print("*"*40)
a = np.identity(3, dtype="int32")
print(a)

"""
random  matrix
"""
print("*"*40)
a = np.random.rand(3,3)
print(a)

print("*"*40)
a = np.random.randint(10,15, size=(3,3))
print(a)