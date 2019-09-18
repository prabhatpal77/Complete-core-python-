#else block should be precided by if or elif or while or for..
#syntax----
# if condition:
#     statement1
#       statement2
#         statement3....
#       ....statementn
# else:
#     statement1
#       statement2
#         statement3...
#       ....statementn
print("enter a positive no.")
i=input()
x = int (i)
if x<10:
    print("given no is 1 digit no")
else:
    print("given no is >= 2 digit no.")
print("end")
