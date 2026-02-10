marks= [67,43,98,65,45,78,69,54,56]

print("Marks of all students")
print(marks)
f_3=[]
l_3=[]
for m in range(3):
    f_3.append(marks[m])

for m in range(len(marks)-3,len(marks)):
    l_3.append(marks[m])  

print("First three marks: ",f_3)
print("last three marks: ",l_3)

print("Highest marks: ",max(marks))
print("Lowest marks: ",min(marks))
print("Average marks: ",sum(marks)/len(marks))