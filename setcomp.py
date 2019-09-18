# the concept of generating element into the set object by writing some logic in the set is known as a set comprehention..
x={p for p in range(10)}
print(x)
y={q**2 for q in range(10, 20) if q%2==0 }
print(y)
z={r*r for r in range(20, 30) if r%2!=0}
print(z)
