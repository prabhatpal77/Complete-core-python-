# Defining user defined exception class, rising that exception explicitly and handle that exception is comes
# under user defined exception implementation..
# program- Gussing random no. in user definee exception.
import random
class ValueTooSmallError(Exception):
    pass
class ValueTooLargeError(Exception):
    pass
number=random.randint(1, 10)
while True:
    try:
        i_num=int(input("enter a number"))
        if i_num<number:
            raise ValueTooSmallError
        elif i_num>number:
            raise ValueTooLargeError
        break
    except(ValueTooSmallError):
        print("This value is too small, try again")
    except(ValueTooLargeError):
        print("This value is too large, try again")
print("congratulation! you gussed is correvtly")
