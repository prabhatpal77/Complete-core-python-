# Built-in module is a pre-define module which contains frequently used pre-define functions, classes, exceptions..
# Even though we import a one module for more then ones and by default that module is imported only once..
import demo1
import imp
b=2000
def f2():
    print("in f2 of test")
print(b)
f2()
print(demo1.a)
demo1.f1()
imp.reload(demo1)
