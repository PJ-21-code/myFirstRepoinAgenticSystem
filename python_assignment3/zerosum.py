n= int(input("Enter a number: "))
sum=0
while(True):
    sum=sum+n
    n= int(input("Enter number: "))
    if(n==0):
        print("Entered Zero.System terminates here.")
        break

print("Final Sum:",sum)    