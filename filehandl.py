# Through the python program we can open the file, perform the operations on the file and we can close the file..
# 'r', 'w', 'a', 't', 'b', '+' for operations on file
# Open function opens the given file into the specified mode and crete file object..
# reading from file...
x=open("myfile.txt")
print(x.read())
x.close()
