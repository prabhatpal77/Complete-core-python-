# In order to handle the different exception by using different exception block we use single try with multiple except block.
print("begin")
x=input("enter fno")
y=input("enter sno")
try:
    i=int(x)
    j=int(y)
    k=i/j
    print(k)
except(ZeroDivisionError):
    print("sno can not be zero")
except(ValueError):
    print("enter numerical value only")
except:
    print("error occured")
print("end")
# While defining single try with multiple except blocks default except blocks should be the last
# except block otherwise we will get error..
