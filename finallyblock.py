# The block which precceded by the finally keyword is known as a finally block.
# try:
# ......
#......
# finally:
#........
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
finally:
    print("welcome")
print("end")
