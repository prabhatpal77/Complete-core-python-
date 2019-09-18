# Global variable:- The variables which are declared outside of all the functions are known as global variables.
# Local variable:- The variables which are declared with in the function body are known as local variables.
a=1000
b=2000
def f1():
    p=3000
    q=4000
    print(a)
    print(b)
    print(p)
    print(q)
def f2():
    x=5000
    y=6000
    print(a)
    print(b)
    print(x)
    print(y)
    print(p)
    print(q)
f1()
f2()
# NameError: name 'p' is not defined
