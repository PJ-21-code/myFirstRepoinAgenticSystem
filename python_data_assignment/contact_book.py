logbook= {
    "Ravi": 9078657434,
    "Avinash": 5698784327,
    "Chirag": 9058956512,
    "Ajay": 9998886655
}
for k,v in logbook.items():
    print(f"{k} : {v}")
name= input("Enter any name you want to search in logbook \n")

if name in logbook:
    print("Contact found. It is ",logbook[name])
else:
    print("Contact not found")    