#elif block should be precided by if or another elif..
i=input("enter a positive no")
x=int(i)
if x<10:
    print("given no is 1 digit no")
elif x<100:
    print("given no is 2 digit no")
elif x<1000:
    print("given no is 3 digit no")
else:
    print("given no is >= 4 digit no")
print("end")
