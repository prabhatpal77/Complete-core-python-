# both default and non-default...
def add(a, b=20):
    c=a+b
    print(c)
add(123)
add(1000, 2000)

# After deffining the default parameter we are not allow to define non-default parameter.
# Otherwise we will get syntax error..
# e.g.-- def add(a=100, b): it will generate syntax error.
