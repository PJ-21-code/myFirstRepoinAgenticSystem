import pandas as pd 

df = pd.read_csv(r"C:\Users\pranj\ASD\myFirstRepoinAgenticSystem\python_logic_assignment\student_score - Sheet1.csv")

print(df['name'])
new_df= df[["name","score"]]

print(new_df)
print("-------------------------------")

first_three= df.iloc[0:3]
print(first_three)
print("-----------------------------")

df_1=df.set_index("name")
first_loc= df_1.loc["Ritu Walia"]
print(first_loc)
print("-------------------------------")

scores= df[df["score"]>85]
print(scores)
print("----------------------------------")

scores_1= df[(df["score"]>85) & (df["passed"]== True)]
print(scores_1)
print("----------------------------------")

sorted_data= df.sort_values("score",ascending=False)
print(sorted_data)
print("-------------------------------------")

print("Top scorers")

top_score= df[df["score"]>=90][["name","score"]].sort_values("score",ascending=False)

print(top_score)