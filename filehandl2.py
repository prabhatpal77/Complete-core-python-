# open a file and perform operations...
x=open("myfile.txt")
print(x.tell())
x.seek(12)
print(x.tell())
print(x.read())
print(x.tell())
x.close()
