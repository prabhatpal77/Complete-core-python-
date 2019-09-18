# set object can be created by using {} or by calling set function...
x={10, 20, 30, 40, 50}
print(x)
print(type(x))
print(len(x))
y=set()
print(y)
print(type(y))
print(len(y))
z={100, 200, 300, 200, 100}
print(z)
p={1000, 123.123, True}
print(p)
a, b, c=p
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(20 in x)
print(123 in x)
for i in x:
    print(i)
