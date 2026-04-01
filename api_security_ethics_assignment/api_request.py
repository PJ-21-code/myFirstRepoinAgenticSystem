import requests
import os
from dotenv import load_dotenv
load_dotenv()

response= requests.get("https://api.example.com/data")

if(response.status_code==200):
    print(response.json())
elif(response.status_code==429):
    print("Rate limit reached. Try again later.") 
else:
    print(f"Request failed. ERROR: {response.status_code}")       

api_key= os.getenv("API_KEY")
print(api_key)    