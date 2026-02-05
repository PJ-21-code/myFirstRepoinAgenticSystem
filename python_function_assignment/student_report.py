name= input("Enter your name: ")

def greet(name):
    return f"Hello {name}!"

marks= [78,89,90,86]
avg=0
def score(report,c,sum):
    for m in report:
        c=c+1
        sum=sum+m
    avg= sum/c
    return c,avg 

def result(avg):
    if avg>=50:
        return "Pass"
    else:
        return "Fail"
    
def main():
    print(greet(name))
    c,avg= score(marks,0,0)
    print("Subjects: ",c)
    print("Average marks: ",avg)
    print("Result: ",result(avg))    

main()    