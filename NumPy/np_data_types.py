import numpy as np

a1 = np.array([1, 2, 3])
print(a1.dtype)

a2 = np.array([1, 2, 3], dtype="int16")
print(a2.dtype)

"""
# one int data required respective bits to store it
np.int8
np.int16
np.int32
np.int64
np.uint8
np.uint16
np.uint32
np.uint64
np.float32
np.float64
np.complex64
np.complex128
"""

a3 = np.array([1, 2, 3], dtype="int16")
a4 = a3.astype("float32")
l1 = a4.tolist()