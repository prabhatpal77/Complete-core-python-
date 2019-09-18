# any parameter which is preceeded by * or ****.....* is known as a arbittary parameter.
# single * arbittary parameter type will be taken as a tuple.
# At the time of calling the function we can pass 0 or mare values to the single star arbittary parameter..
def add(*a):
    print(a)
    print(type(a))
    print(len(a))
    s=0
    for p in a:
        s=s+p
    print(s)
add()
add(1000, 2000, 3000)
add(10, 20, 30, 40, 50, 60)
