number=[]

with open("numbers.txt","r") as file:
    number= file.readlines()
list_num= list(map(int,number))
#print(list_num)
sum=0
for n in list_num:
    sum=sum+n
count= len(list_num)    
avg= sum/count


with open("result.log",  "a") as log_file:
    log_file.write(f"File opened successfully\n")
    log_file.write(f"Read {count} numbers\n")
    log_file.write(f"Sum is {sum}\n")
    log_file.write(f"Average is {avg}\n")