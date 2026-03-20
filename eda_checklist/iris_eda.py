import pandas as pd
import plotly.express as px

df= pd.read_csv(r"C:\Users\pranj\ASD\myFirstRepoinAgenticSystem\eda_checklist\iris.csv")

print(df.head())
print(df.shape)

print(df.info())

print("Missing values:")
print(df.isnull().sum())

fig= px.histogram(
    df,
    x="sepal.length",
    nbins=10,
    title="Distribution of sepal length"
)


fig.show()

outliers= px.box(
    df,
    x="variety",
    y="sepal.width",
    title="Outliers"
)

outliers.show()

corr= df[['petal.length','petal.width']].corr(numeric_only=True)

fig3= px.imshow(
    corr,
    text_auto=True,
    title="Correlation analysis between petal length and petal width"
)

fig3.show()

corr_full= df.corr(numeric_only=True)

fig_correlation= px.imshow(
    corr_full,
    text_auto=True,
    title= "Crrelation heatmap"
)

fig_correlation.show()

