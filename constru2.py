#constructor;
class A:
    def __init__(self):
        self.a=int(input("Enter rollno:"))
        self.b=input("Enter Name:")
    def value(self):
        m1=int(input("Enter m1:"))
        m2=int(input("Enter m2:"))
        m3=int(input("Enter m3:"))
        tot=m1+m2+m3
        print("Total:",tot)
x=A()
x.value()
