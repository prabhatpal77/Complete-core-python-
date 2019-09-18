# operation like copy, pop, popitem, in dictionary type....
x={"java":80, "python":99, "hadoop":87}
print(x)
x["aws"]=78
print(x)
y=x.copy()
print(y)
x.pop("hadoop")
print(x)
x.popitem()
print(x)
x.clear()
print(x)
