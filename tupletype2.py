# for and while in tuple..
x=(10, 20, 30, 40, 50, 60)
print(x)
print(20 in x)
print(123 in x)
for p in x:
    print(p)
i=0
while i<len(x):
    print(x[i])
    i=i+1
y=(1000, 123.123, True)
print(y)
a, b, c=y
print(a, type(a))
print(b, type(b))
print(c, type(c))
