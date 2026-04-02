import requests
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

response= requests.get("https://jsonplaceholder.typicode.com/posts")

if response.status_code==200:
    data= response.json()

df= pd.DataFrame(data)    

df= df.rename(columns={"userId": "user_id"})
df= df.drop(columns=['id'])

post_count= df.groupby("user_id").size()
df['post_length']= df['body'].apply(len)

st.title("Post Dashboard")
st.write("User post data")
st.dataframe(df.head(20))

st.write("post per user")
st.bar_chart(post_count)

fig= px.histogram(df, x='post_length', nbins=30)
st.write("post length distribution")
st.plotly_chart(fig)