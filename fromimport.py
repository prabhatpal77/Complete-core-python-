#By using from import we can import only reqired properties of the module instead of import on 'n' type module object..
from demo import a, f1
from math import pi, sqrt
b=2000
def f2():
    print("in f2 of test")
print(b)
f2()
print(a)
f1()
print(pi)
p=sqrt(100)
print(p)
# At the time of importing the properties of a module by using from impoert we can use *.
# From import with * will degrate the performence of the application so that we never
# recommend to use from import with *.
# eg:- from demo import *
#      from math import *
