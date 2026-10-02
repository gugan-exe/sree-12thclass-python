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
  

