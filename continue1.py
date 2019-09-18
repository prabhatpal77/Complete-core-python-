# whenever control reached to the continue statement of a loop in any iteration then without executing
# remmining statement of that itteration control will goes to the next iteration.
print("begin")
i=0
while i<=5:
    i=i+1
    if i==3:
        continue
    print("welcome",i)
else:
    print("in while else")
print("end")
