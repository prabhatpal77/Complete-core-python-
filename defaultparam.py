# The parameters which are declared by assigning the value are known as default parameters.
# At the time of calling the function we need not to pass the values to the default parameters..
def add(a=10, b=20):
    c=a+b
    print(c)
add()
add(123)
add(1000, 2000)
