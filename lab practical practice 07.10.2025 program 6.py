student={}
def add():
    name=(input("Enter your name: "))
    marks=int(input("Enter yours marks: "))
    student[name]=marks
def display():
    print("Name\t\tMarks")
    for i in student:
        print(i,"\t\t",student[i])
def update():
    name=(input("Enter the name for update: "))
    if name in student:
        marks=int(input("Enter the new marks: "))
        student[name]=marks
        print("for",name,"marks updated to",marks)
    else:
        print("sorry! no record found")
def delete():
    name=(input("Enter the name for deletion: "))
    if name in student:
        del student[name]
        print("Record deleted")
    else:
        print("Sorry no record found")
# main program
while True:
    print("1 Add Student")
    print("2 Display Student")
    print("3 Update Student")
    print("4 Delete Student")
    print("5 Exit")
    n=int(input("Enter your choice: "))
    if n==1:
        add()
    if n==2:
        display()
    if n==3:
        update()
    if n==4:
        delete()
    if n==5:
        break
    else:
        print("Invalid Option")
