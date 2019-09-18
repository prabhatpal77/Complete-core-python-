#if we don't define any return statement sxplicitly with in the function or if user define return statement
# is not executed bydefault a function return the default value called none:
def add(a, b):
    c=a+b
    print(c)
p=add(1000, 2000)
print(p)
