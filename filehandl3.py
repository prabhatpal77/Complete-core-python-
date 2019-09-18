#reading line by line...
x=open("myfile.txt")
lines=x.readlines()
print(lines)
for p in lines:
    print(p, end=" ")
x.close()
