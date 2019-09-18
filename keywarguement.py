# Arguement which we are passing by assigning to the parameters names are known as keyword arguement or
# non-positional arguement..
def myfunc(name, msg):
    print("hello", name, msg)
myfunc(name="prabhat pal", msg="good morning")
myfunc(msg="good morning", name="prabhat pal")
# After passing the keyword arguement we are not allow to pass non-keyword arguements. otherwise we will
# get syntax error..
