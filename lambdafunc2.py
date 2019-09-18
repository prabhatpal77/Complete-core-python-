#cube
def cube(a, func):
    p=func(a)
    return a*p
res=cube(10, lambda b:b*b)
print(res)
