# Recursive function invokation:- The function which is called by itself is known as a recursive function invitation.
# Python supports recursive function invitation but it will not supports infinite recursion..
def myfunc():
    print("welcome")
    myfunc()
myfunc()
# RecursionError: maximum recursion depth exceeded while calling a Python object
