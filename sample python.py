import pickle
file=open(r"C:\Users\SSS Family\OneDrive\Desktop\sample text.txt","r")
readinfo=file.read(100)
print(readinfo)
readinfo2=file.read(1000)
print(readinfo2)
file2=open(r"C:\Users\SSS Family\OneDrive\Desktop\sampletext2.txt","w")
writing=file2.write("Hello India! \n Hello")
file2.close()

fb=open(r"C:\Users\SSS Family\OneDrive\Desktop\samplebinary.dat","wb")
services=["editing","content_making","uploading"]
pickle.dump(services,fb)
#fr=open(r"C:\Users\SSS Family\OneDrive\Desktop\samplebinary.dat","rb")
#s=pickle.load(fr)
#print(s)
#fb.close()

