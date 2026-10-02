def writefile():
    f=open('sample.txt','w')
    n=int(input("Enter the no. of lines you want to store in the file: "))
    for i in range(n):
        s=input ("Enter a line of text")
        f.write(s)
        f.write('\n')
        print('Line stored successfully')
    f.close()
def readfile():
    f=open("sample.txt",'r') 
    print("\nThe contents of the file is: ")
    for i in f:
        print (i, end='#')
        print()
    f.close()
#main program
writefile()
readfile()
