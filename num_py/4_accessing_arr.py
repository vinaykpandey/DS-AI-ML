"""
arr[index] one dimensional array
arr[row][column] two dimensional array
"""
import numpy as np

a1 = np.array([[1, 2, 3], [10, 20, 30]], dtype="int16")
print(a1.ndim)
print(a1.shape)
print(a1[0][0])
print(a1[0][1])
print(a1[1][1])
print(a1[1, 2])
a1[1] = [11, 21, 31]  # update 1st rwo
print(a1)

"""
slice operator
beg:end:step
"""
a2 = a1[::,0]
print(a2)




