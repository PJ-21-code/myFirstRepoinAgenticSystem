n= int(input("Enter a number: "))

def checker(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
    
print(f"Number is {checker(n)}")    