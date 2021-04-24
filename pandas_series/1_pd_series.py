import pandas as pd
import numpy as np

data = ["Varanasi", "Prayagraj", "Mathura", "Delhi", "Mumbai", "Goa"]
index = ['v', 'p', 'm', 'd', 'm', 'g']
a = pd.Series(data)
# print(a)  # index, value

a = pd.Series(data, index)
# print(a)  # index, value

d1 = (10, 20, 30, 40, 50)
b = pd.Series(d1)
# print(b)


d1 = (10, 20, 30, "hi", 50)
b = pd.Series(d1)
# print(b)


data_dict = {1: "Vns", 2: "Prg", 3: "Mth", 4: "Dl"}
a = pd.Series(data_dict)
print(a)

a1 = np.array([[1, 2, 3], [10, 20, 30]], dtype="int16")
a2 = np.array([[11, 12, 13], [11, 21, 31]], dtype="int16")
index = (0, 1)
data = (a1, a2)
a = pd.Series(data)
print(a)

b1 = pd.Series(a1)  # Exception: Data must be 1-dimensional
