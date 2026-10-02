f = open ("sample1.txt", "r")
a= f.read()
for i in a.split():
    if i[-1]=="e":
        print(i,end=" ")
f.close()
