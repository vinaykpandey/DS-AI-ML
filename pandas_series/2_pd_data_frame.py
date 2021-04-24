import pandas as pd
import numpy as np

d1 = {0: 'a', 1: 'b', 2: 'c'}
d2 = {0: 'Anna', 1: 'Bikas', 2: 'Chatur'}
data = {"first": d1, "second": d2}
s = pd.Series(data)
print(s)
df = pd.DataFrame(data)
print(df)

print("*" * 40)
a1 = np.array([[1, 2, 3], [10, 20, 30]])
df1 = pd.DataFrame(a1)
print(df1)

print("*" * 40)

s1 = pd.Series([1, 3, 5, 7, 9])
s2 = pd.Series([2, 4, 6, 8, 10])
s3 = pd.Series([3, 6, 9, 12, 15])
data_dict = {"s1": s1, "s2": s2, "s3": s3}

df_2 = pd.DataFrame(data_dict)
print(df_2)
df_2.index = ["a", "b", "c", "d", "e"]
print(df_2)

df = pd.read_csv("../plot/pd_data.csv")
print(df)
