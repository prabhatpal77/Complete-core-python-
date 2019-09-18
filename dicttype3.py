# dictionary with keys, values and duplicate values...
x={"java":80, "python":99, "hadoop":87}
print(x)
for p in x:
    print(p, x[p])
print("python" in x)
print("aws" in x)
print(99 in x)
k=x.keys()
for q in k:
    print(q)
v=x.values()
for r in v:
    print(r)
kv=x.items()
for i in kv:
    print(i[0], i[1])
for a,b in kv:
    print(a,b)
