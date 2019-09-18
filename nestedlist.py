#lists inside the list...
x=[[10, 20, 30],[40, 50, 60, 99],[70,80,90]]
print(x)
for p in x:
    for q in p:
        print(q, end=" ")
    print()
y=[[10, 20, 30],[40, 50, 60],[70, 80, 90]]
print(y)
for a, b, c in y:
    print(a, b, c)
