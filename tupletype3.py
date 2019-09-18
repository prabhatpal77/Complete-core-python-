# nested tuple with for loop..
x=(10, 20, 30, 40, 50, 60)
print(x)
print(x.count(20))
print(x.count(75))
print(x.index(40))
y=((10, 20, 30),(40, 50, 60),(70, 80, 90))
print(y)
for p in y:
    for q in p:
        print(q, end=" ")
    print()
for a, b, c in y:
    print(a, b, c)
z=((10, 20, 30),[40, 50, 60],(70, 80, 90))
print(z)
z[1][1]=99
print(z)
