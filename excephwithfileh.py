# Exception handling with file handling....
x=None
try:
    x=open("myfile.txt")
    print("file is openned")
    print(x.read())
    x.write("hello world")
except:
    print("error occured")
finally:
    if x!=None:
        x.close()
        print("file is closed")
