def factorial():
    n=int(input("Enter the number: "))
    fact=1
    while (n>0):
        fact=fact*n
        n=n-1
        print(fact,"is the factorial of the number of",n)
factorial()
def palindrome():
    text=input("Enter your text: ")
    if text==text[::-1]:
        print("The entered is palindrome")
    else:
        print("THe entered text is not palindrome")
palindrome()    
