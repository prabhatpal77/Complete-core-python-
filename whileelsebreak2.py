# Generally we use the break statement for exit from infinite loops...
print("begin")
i=1
while True:
    print("welcome",i)
    if i==5:
        break
    i=i+1
print("end")
