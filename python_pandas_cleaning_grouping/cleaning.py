import pandas as pd
import numpy as np

# Creating sample dataset
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)
print("Dataset")
print("------------------------")
print(df)

print("Null values")
print("------------------------")
print(df[df["Salary"].isnull()])

print("Filling missing values")
print("------------------------")
df= df["Salary"].fillna(df["Salary"].mean())
print(df.head())

print("Dropping temporary notes column")
print("-------------------------")
df= df.drop(columns="Temporary_Notes",axis=1)
print(df.head())

print("Renaming salary to annual_salary")
print("---------------------------------")
df= df.rename(columns={"Salary":"Annual_Salary"})
print(df.head(3))

print("Grouping data by department")
print("----------------------------")
print("Company Data Summary")
print("----------------------------")
summary_df= df.groupby("Department").agg({"Annual_Salary":["mean"], "Employee":["count"]})
print(summary_df)
print("Whole dataset after changes")
print("----------------------------")
print(df)