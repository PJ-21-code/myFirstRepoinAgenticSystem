import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

response= requests.get("https://jsonplaceholder.typicode.com/posts")

if response.status_code==200:
    data= response.json()

df= pd.DataFrame(data)    

#data cleaning
df= df.rename(columns={"userId": "user_id"})
df= df.drop(columns=['id'])

print(df.head())

#post_count
post_count= df.groupby("user_id").size()
print(post_count)

#length of each post
df['post_length']= df['body'].apply(len)
print(df.head())
plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
post_count.plot(kind="bar")
plt.title("Post made by each user")
plt.xlabel("users")
plt.ylabel("no of posts")

plt.subplot(1,2,2)
plt.hist(df['post_length'],color='blue',edgecolor='black')
plt.title("Post length distribution")
plt.xlabel("post_length range")
plt.ylabel("no of posts")

plt.show()