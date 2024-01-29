class A:
    print("Multiple Inheritance")
    def __init__(self):
        self.r=int(input("Rollno:"))
        self.n=input("Name:")
        self.a=input("Address:")
class B:
    def marks(self):
        self.m1=int(input("Mark1:"))
        self.m2=int(input("Mark2:"))
        self.m3=int(input("Mark3:"))
        self.m4=int(input("Mark4:"))
        self.m5=int(input("Mark5:"))
    def total(self):
        self.tot=(self.m1+self.m2+self.m3+self.m4+self.m5)
        print("Total:",self.tot)
        self.avg=self.tot/5
        print("Avg:",self.avg)
class C(A,B):
    def bio(self):
        print("Roll:",self.r)
        print("Name:",self.n)
        print("Address:",self.a)
        print("Total:",self.tot)
        print("Avg:",self.avg)
ob=C()
ob.marks()
ob.total()
ob.bio()
