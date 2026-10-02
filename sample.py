f=open("sample.txt","w+")
S=[]
for i in range(0,5):
    name=input("Enter the student name: ")
    S.append(name + "\n")
    f.writelines(S)
L=f.read(50)
print(L)
f.close()
