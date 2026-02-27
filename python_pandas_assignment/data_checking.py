import pandas as pd

df= pd.read_csv(r"C:\Users\pranj\ASD\myFirstRepoinAgenticSystem\python_pandas_assignment\salary_data.csv")

first_5= df.head()
last_5= df.tail()
information= df.info()
statistical_des= df.describe()

salary= df['Salary']

x= df[['YearsExperience','Salary']]

good_salary= df[df['Salary']>100000]

print("First 5 rows")
print("------------")
print(first_5)
print("------------")

print("Last 5 rows")
print("------------")
print(last_5)
print("------------")

print("Data Information")
print("------------")
print(information)
print("------------")

print("Statistical description")
print("------------")
print(statistical_des)
print("------------")

print("Salary:")
print(salary)
print("---------")

print(x)

print("Salaries Above 100000")
print(good_salary)

