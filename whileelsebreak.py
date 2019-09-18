# While control reached to the break statement of a loop without execution remmining statement of the iteration
# and remmining iteration controls will comes from the loop execution...
print("begin")
i=1
while i<=5:
    print("welcome",i)
    if i==3:
        break
    i=i+1
else:
    print("while else")
print("else")
