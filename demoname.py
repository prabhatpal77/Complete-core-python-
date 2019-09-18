# use of __name__=="__main__" in python
print("welcome")
print("demoname module name is ",__name__)
a=1000
def f1():
    print("in f1 of demo")
if __name__=="__main__":
    print(a)
    f1()
