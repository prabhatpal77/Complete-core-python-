# multistar arbittary parameter type will be taken as a dectionary..
# Dictionary can store the 0 or more items. At the time of calling the function we can pass 0or more items
# to the multistar arbittary parameter.
def myfunc(**a):
    print(a)
    print(type(a))
    print(len(a))
myfunc()
myfunc(name="prabhat", desg="consult")
myfunc(a=10, b=20, c=30, d=40)
