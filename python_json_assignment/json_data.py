import json

data= '''
{
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}
'''   

dict_data= json.loads(data)
print(type(dict_data))
if dict_data["result"]["confidence"] <0.9:
    print("WARNING : Low confidence score!")
    print("-------------------------------")

print(dict_data)
print("---------------------")
print("Follow up response")
d_data={}
d_data["id"]= dict_data["id"]
d_data["status"]= dict_data["status"]
d_data["text"]= dict_data["result"]["text"]
d_data["confidence"]= dict_data["result"]["confidence"] 

for k,v in d_data.items():
    print(f"{k} : {v}") 

with open("response.json","w") as f:
    json.dump(d_data,f)