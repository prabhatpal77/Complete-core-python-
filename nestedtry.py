# We can define once try block inside another try.
# A try block which contain another try block is known as a outer try block or inclosing try block..
# The try block which is defining another try block is known as a inner try block or nested try block..
try:
    print("in try1")
    try:
        print("in try2")
    except(ZeroDivisionError):
        print("in except2")
    finally:
        print("in finally2")
except(KeyError):
    print("in except1")
    try:
        print("in try3")
    except(ValueError):
        print("in except3")
    finally:
        print("in finally3")
finally:
    print("in finally1")
    try:
        print("in try4")
    except(IndexError):
        print("in exception4")
    finally:
        print("in finally4")
