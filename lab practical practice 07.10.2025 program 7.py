import random
start=int(input("Enter the start number of the ticket: "))
end=int(input("Enter the end number of te ticket: "))
n=int(input("Enter number of draws you need: "))
for i in range(1,n+1):
    winner=random.randint(start,end)
    print("prize",i,":",winner)
