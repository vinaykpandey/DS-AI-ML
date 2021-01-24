import numpy as np
print(np)

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype="float32")

print(a.ndim)

print(a.size)

print(a.mean())

print(a.prod())

print(a.reshape([9,1]))

print(a.sum())

print(a.shape)



print(a.transpose())

print(a.trace())

b = a
print(a+b)

print(a*b)

print(a+2)

print(a-3)

print(a/2)

print(np.matmul(a, b))
np.average(a)
print("*"*40)
# open a file in numpy arr
a = np.genfromtxt("data.txt", delimiter=",")
print(a)
