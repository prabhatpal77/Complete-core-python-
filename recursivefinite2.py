# factorial of any number using recursion...
def recur_fact(x):
    if x==1:
        return 1
    else:
        return (x*recur_fact(x-1))
num=int(input("Enter a number:"))
if num>=1:
    res=recur_fact(num)
    print("factorial of",num,"is",res)
