# split method in python..
x='python is an opensource language'
print(x)
words=x.split()
for w in words:
    print(w)
y='python@is@an@opensource@language'
print(y)
res=y.split("@")
for q in res:
    print(q.lower(), q.upper(), len(q))
