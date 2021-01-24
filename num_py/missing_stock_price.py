import numpy as np
from scipy import interpolate

n = int(input())
prices = []
for i in range(n):
    time, price = input().split("\t")
    prices.append(price)
x = []
prices_float = []
x_unknown = []
for i in range(n):
    if not "Missing" in prices[i]:
        x.append(i)
        prices_float.append(float(prices[i]))
    else:
        x_unknown.append(i)
y = np.array(prices_float)
f = interpolate.UnivariateSpline(x, y, s=1)

for i in x_unknown:
    print(f(i))
