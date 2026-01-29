balance= int(input("Enter the balance amount of your bank account: "))
withdraw= int(input("Enter amoount you want to withdraw: "))

status= input("Verification Status : (True/False): ")

if(status!="True" and status!="False"):
    print("Enter the verification status again")
    status= input()

if(withdraw<=balance and status=="True"):
    print(f"Withdrawal Successful. Amount left in account: {balance-withdraw}")
else:
    print("Transaction denied!")    