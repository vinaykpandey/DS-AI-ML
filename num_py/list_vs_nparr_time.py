'''
We'll see why numpy is very popular and talk about its
main feature "n dimensional array". It is memory efficient,
fast and convenient compared to python native list.
h
'''
import numpy as np
import time
import sys

SIZE = 100000
l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

start = time.time()
res_list = [(x + y) for x, y in zip(l1, l2)]
print("list took: ", (time.time() - start) * 100)

start = time.time()
result_numpy = a1 + a2
print("numpy array took: ", (time.time() - start) * 100)
