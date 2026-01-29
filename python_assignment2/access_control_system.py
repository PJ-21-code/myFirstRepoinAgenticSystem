age = int(input("Enter your age: "))
id= (input("Do you have your ID Card? write(True/False): "))

if(id!="True" and id!="False"):
    print("Enter your answer again! Do you have your ID card?")
    id=(input())

if(age>=18 and id=="True"):
    print("Entry Allowed")
else:
    print("Entry not allowed")    