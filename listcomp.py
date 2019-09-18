# list comperihentions generating elements into the list object by writting some logic in the list is known
# as a list comperihention...
x=[p for p in range(10)]
print(x)
y=[q**2 for q in range(10, 20) if q%2==0]
print(y)
z=[r*2 for r in range(20, 30) if r%2!=0]
print(z)
