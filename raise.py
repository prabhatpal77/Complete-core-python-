# raise is a statement, is used to raise the exception explecitly..
print("begin")
x=input("enter fno")
y=input("enter sno")
try:
    i=int(x)
    j=int(y)
    k=i/j
    print(k)
    raise KeyError
except(ZeroDivisionError):
    print("sno can not be zero")
except(ValueError):
    print("error occured")
except:
    print("error occured")
print("end")
