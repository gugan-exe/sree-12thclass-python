def countword(text,word):
    s=text.split()
    count=0
    for w in s:
        if w==word:
            count+=1
    return count
#main program
text=input("Enter the Sentence: ")
while True:
    word=input("Enter the word to search in sentence: ")
    count=countword(text,word)
    if count==0:
        print("Sorry, the word is not present in the sentence!")
    else:
        print("THe word occurs",count,"times")
        ans=input("So you want to continue the search(Y/N):")
        if ans not in("Y","y"):
            break
