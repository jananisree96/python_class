#constructor:
class sam:
    def __init__(self):
        self.n=input("Enter your name:")
        self.a=int(input("Enter your age:"))
        self.p=input("Enter your address:")
        self.c=input("Enter your course:")
    def display(self):
        print("Name:",self.n)
        print("Age:",self.a)
        print("Address:",self.p)
        print("Course:",self.c)
ob=sam()
ob.display()
