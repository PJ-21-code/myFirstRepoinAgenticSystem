import requests

params={
    'q':'python',
    'sort':'stars',
    'order':'desc',
    'per_page':5
}

response= requests.get("https://api.github.com/search/repositories",params=params)
print(response.status_code)

if response.status_code==200:
    data= response.json()
    #print(data)
print(f"Total_repositories: {data["total_count"]}")
items= data['items']
print("Top 5 python repositories:")
for item in items:
    print(f"{item['name']} & No of stars:{item['stargazers_count']}")

