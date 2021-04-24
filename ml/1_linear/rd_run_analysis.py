import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

# Import the excel file and call it xls_file
excel_file = pd.ExcelFile('dravid_year_wise_run_1996_to_2011.xlsx')

# View the excel_file's sheet names
print(excel_file.sheet_names)

# Load the excel_file's Sheet1 as a dataframe
df = excel_file.parse('year-runs')
print(df)
year_list = df.year
run_list = df.runs
total_run_list = df.total_runs
plt.xlabel('year')
plt.ylabel('runs')
plt.ylabel('total_runs')
plt.plot(year_list, run_list, color='red', marker='*')
plt.plot(year_list, total_run_list, color='blue', marker='.')
df_x = pd.DataFrame(df.year)
reg_run = linear_model.LinearRegression()
reg_total_run = linear_model.LinearRegression()
reg_run.fit(df_x, run_list)
reg_total_run.fit(df_x, total_run_list)
print(reg_run.coef_, reg_run.intercept_)
print(reg_total_run.coef_, reg_total_run.intercept_)
print("current year run ", reg_run.predict([[2012]]))
print("total year run ", reg_total_run.predict([[2012]]))
