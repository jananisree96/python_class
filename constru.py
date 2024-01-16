#constructor:
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def value(self):
        m1=int(input("Enter mark1:"))
        m2=int(input("Enter mark2:"))
        m3=int(input("Enter mark3:"))
        tot=m1+m2+m3
        print("Rolno:",self.a)
        print("Name:",self.b)
        print("Total:",tot)
x=A(121,"Selva")
x.value()
