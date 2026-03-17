n = int(input("Enter number of students: "))
d = {}

for i in range(n):
    name = input("Enter student name: ")
    marks = input("Enter student marks: ")
    d[name] = marks

while True:
    name = input("Enter student name to get marks: ")
    marks = d.get(name, -1)

    if marks == -1:
        print("Student not found")
    else:
        print("The marks of", name, "are", marks)

    option = input("Do you want to search another student (yes/no): ")
    if option == "no":
        print("Thanks for using this application")
        break