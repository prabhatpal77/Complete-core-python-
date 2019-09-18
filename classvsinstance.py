# class vs instance
class Person:
    def __init__(self, initialAge):
        if initialAge>0:
            self.age=initialAge
        else:
            print("Age is not valid, setting age to 0.")
            self.age=0
    def amIold(self):
        if self.age<13:
            print("You are young")
        elif self.age<18:
            print("you are a teenager")
        else:
            print("you are old")
    def yearPasses(self):
        self.age+=1
    t=int(input())
    for i in range(0, t):
        age=int(input())
        p=person(age)
        p.amIold()
        for j in range(0,3):
            p.yearPasses()
        p.amIold()
        print(" ")
