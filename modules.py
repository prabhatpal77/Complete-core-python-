# Every python file itself is known as one module...
# python supports 2 types of import statements. 1. Normal import, 2. From import
# import demo.py in this file also..
import demo as x
import math as y
b=2000
def f2():
    print("in f2 of test")
print(b)
f2()
print(x.a)
x.f1()
print(y.pi)
p=y.sqrt(1000)
print(p)
