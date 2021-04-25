import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

excel_file = pd.ExcelFile('data.xlsx')
print(excel_file.sheet_names)
df = excel_file.parse('Y_sq_x')
x_list = df.x
y_list = df.y

plt.xlabel('x')
plt.ylabel('y')
plt.scatter(x_list, y_list, color='red', marker='*')
df_x = pd.DataFrame(x_list)  # converting list(x) into dataframe(df_x)
reg = linear_model.LinearRegression()
reg.fit(df_x, y_list)
print(reg.coef_, reg.intercept_)
print(reg.predict([[20]]))
