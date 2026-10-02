f=open("marks.txt","w")
count=int(input("Enter the number of students: "))
for i in range(count):
    rollno=int(input("Enter the Student roll No: "))
    name=input("Enter the Student name: ")
    marks=(input("Enter the Student marks: "))
    rec= str(rollno) + "," + name + "," + marks + " "
    f.writelines(rec)
f.close()
