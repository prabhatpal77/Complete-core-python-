# Try block:- Try block is preceeded by try keyword is known as a try block..
# syntax:- try:
#              stmt1
#              stmt2...
#         .....stmtn
# Except block:- A block which is preceeded by the except keyword os known as a except block...
#syntax:- try:
#             stmt1
#             stmt2
#             stmt3.....
#        .....stmtn
#          except(Exceptionclassname):
#             stmt1
#             stmt2
#             stmt3.....
#        .....stmtn
print("begin")
x=input("enter fno")
i=int(x)
y=input("enter sno")
j=int(y)
try:
    k=i/j
    print(k)
except(ZeroDivisionError):
    print("sno can not be zero")
    print("end")
