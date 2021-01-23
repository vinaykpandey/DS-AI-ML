'''
We'll see why numpy is very popular and talk about its
main feature "n dimensional array". It is memory efficient,
fast and convenient compared to python native list.
h

'''
import sys

import numpy as np

# create a list with thousand/1000 element in it
l = range(1000)

# here 5 is any number between 0-999 : bytes consume 28000 byte
print(
    "list size: {}".format(sys.getsizeof(5) * len(l))
)
""""
size of one python object list is 24 byte (64 byte Architecture)
"""

# arrange is function to create array element 0-999 : bytes consume 8000 byte
num_py_arr = np.arange(1000)

print(
    "np array size: {}".format(
        num_py_arr.size * num_py_arr.itemsize
    )
)
""""
size of one  numpy python object list is 8 byte (64 byte Architecture)
"""
