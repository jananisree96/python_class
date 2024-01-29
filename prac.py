class A:
    print("Single inheritance")
    def __init__(self):
        self.a=75
        self.b=5
    def result(self):
        c=self.a+self.b
        print("Add:",c)
        c=self.a-self.b
        print("Sub:",c)
        c=self.a*self.b
        print("Mul:",c)
        c=self.a/self.b
        print("Div:",c)
        c=self.a%self.b
        print("Mod:",c)
class B(A):
    def dis(self):
        print("This is derived class of base class")
ob=B()
ob.result()
ob.dis()
