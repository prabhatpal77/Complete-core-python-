# import demoname file in this file...
import demoname
print("test module name is",__name__)
b=2000
def f2():
    print("in f2 of test")
print(b)
f2()
print(demoname.a)
demoname.f1()
