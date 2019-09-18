# When ever we open a file by using block it will be closed automatically when ever control comes ou from the with block..
with open("myfile.txt") as x:
    print(x.read())
