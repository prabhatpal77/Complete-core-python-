#list with list predefine methods as append(), insert(), copy(), .....
x=[10, 20, 30, 40, 50, 60]
print(x)
x.append(70)
print(x)
x.insert(2, 90)
print(x)
y=x.copy()
print(y)
print(x.index(50))
print(x.count(40))
x.remove(30)
print(x)
x.pop(5)
print(x)
z=[100, 90, 110]
print(z)
x.extend(z)
print(x)
x.sort()
print(x)
x.reverse()
print(x)
x.clear()
print(x)