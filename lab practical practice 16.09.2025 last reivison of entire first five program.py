def factorial():
    n=int(input("Enter the number: "))
    fact=1
    while (n>0):
        fact=fact*n
        n=n-1
    print("Factorial of number is",fact)
def palindrome():
    text=input("Enter the text: ")
    if text==text[::-1]:
        print("The text is palindrome")
    else:
        print("The text is not palindrome")
factorial()
palindrome()
def area_program():
#function definition
    def area_circle(r):
        return (3.14) * (r**2)
    def area_square(a):
        return a*a
    def area_rectangle(a,b):
        return a*b
#main program
    print("AREA OPERATIONS\n1.AREA OF SQUARE\n2.AREA OF CIRCLE\n3.AREA OF RECTANGLE")
    while True:
        ch=int(input("Enter Your Choice: "))
        if ch==1:
            a=int(input("Enter the side of square: "))
            print("area of square is",area_square(a))
        elif ch==2:
            r=int(input("Enter the radius of circle: "))
            print("area of circle is",area_circle(r))
        elif ch==3:
            a=int(input("Enter the side of rectangle: "))
            b=int(input("Enter the side of rectangle: "))
            print("area of rectangle is",area_rectangle(a,b))
        else:
            print("WRONG CHOICE SELECTED")
            break
area_program()
def perfect_number(p):
    sum=0
    for x in range(1,p):
        if p % x == 0:
            sum+=x
    return sum==p
p=int(input("Enter the number for perfect number checking operation: "))
print(perfect_number(p))
def occurences(word,t):
    s=t.split()
    count=0
    for w in s:
        if w==word:
            count+=1
    return count
t=input("Enter the text for count function: ")
while True:
    word=input("Enter the word to search in the text: ")
    count=occurences(word,t)
    if count==0:
        print("Sorry the word is in not in the text")
    else:
        print("Entered word is",count,"times")
        ans=input("Do you want to continue searching...")
        if ans not in ("Y","y"):
            break

