users= ["Nakul","Vansh","Ajay","Chirag","Viraj"]

user_1= {
    "name": "Nakul",
    "scores": [98,89,78],
    "roles": {"admin","viewer"}
}
user_2= {
    "name": "Vansh",
    "scores": [98,89,68],
    "roles": {"admin","viewer"}
}
user_3= {
    "name": "Ajay",
    "scores": [90,67,78],
    "roles": {"tester","viewer"}
}
user_4= {
    "name": "Chirag",
    "scores": [80,60,70],
    "roles": {"viewer"}
}
user_5= {
    "name": "Viraj",
    "scores": [88,89,56],
    "roles": {"admin","viewer","manager"}
}

user_id= (user_1,user_2,user_3,user_4,user_5)
def score_checker(users,user_id):
    for id in user_id:
        if id["name"] in users:
            m= sum(id["scores"])/len(id["scores"])
            id["average"] = m

def access(user_id):
    for id in user_id:
        if "admin" in id["roles"]:
            id["Access"]= "Yes"
        else:
            id["Access"]= "No"    


def main():
    score_checker(users,user_id)
    access(user_id)
    for id in user_id:
        print("name: ",id["name"])
        print("Average score: ",id["average"])
        print("Admin Access: ",id["Access"])

        print("---------------------------")
print("-------Details of users--------")        
main()