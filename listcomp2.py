# list comperihention and nested list...
x="python is a opensource language"
print(x)
words=x.split()
res=[[w.upper(), w.lower(), len(w)] for w in words]
print(res)
for p in res:
    print(p)
