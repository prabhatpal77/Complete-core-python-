#list collection type with loop and if statement...
x=[10, 20, 30, 40, 50, 60]
print(x)
while True:
    i=int(input("enter search element"))
    if i in x:
        print("element is found")
    else:
        print("element is not found")
    break
