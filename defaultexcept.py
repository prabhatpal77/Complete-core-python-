# Default except block is a except block which can handle any type of exception..
x=input("enter fno")
y=input("enter sno")
try:
    i=int(x)
    j=int(y)
    k=i/j
    print(k)
except:
    print("error occured")
print("end")
