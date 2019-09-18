# arbittary parameter with default parameter..
def myfunc(*a, b=123):
    print(a)
    print(b)
myfunc(10, 20, 30,40)
