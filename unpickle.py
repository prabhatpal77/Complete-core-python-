# The concept of getting back the object from the file into the python program and converting that object
# in the form of file supportd format is known as a unpickling..
import pickle
x=open("pickle.txt","rb")
data=pickle.load(x)
for p in data:
    print(p)
x.close()
