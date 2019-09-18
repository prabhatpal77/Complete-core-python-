# sorting in nested list...
x=[[7788, "book", 500.00],[7902,"iphone", 75000.00],[7369, "bottle", 700.00]]
print(x)
for p in x:
    print(p)
    x.sort(key=lambda y:y[1])
    print("after sorting")
    for q in x:
        print(q)
