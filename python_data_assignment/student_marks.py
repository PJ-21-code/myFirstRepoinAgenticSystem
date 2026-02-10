marks= [67,43,98,65,45,78,69,54,56]

print("Marks of all students")
print(marks)

print("First three marks: ",marks[:3])
print("last three marks: ",marks[len(marks)-3:])

print("Highest marks: ",max(marks))
print("Lowest marks: ",min(marks))
print("Average marks: ",sum(marks)/len(marks))