password= input("Enter password: ")
ori_pass= "admin123"

while(ori_pass!=password):
    print("Wrong password. Enter Again")
    password= input()

print("Access granted")    