n = int(input("Enter the number of students: "))
d = {}
for i in range(n):
    name = input("Enter student name: ")
    marks = input("Enter student marks: ")
    d[name] = marks

while True:
    name = input("Enter student name to get marks: ")
    marks = d.get(name,-1)
    if marks == -1:
        print("Student not found.")
    else:
        print("The marks of ",name," are ",marks)
    
    option = input("Do you want to find another student's marks? [Y/N]")
    if option == "N":
        break

print("Thanks for using the application!")
