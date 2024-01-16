#class and object using self method:

class op:
    n1=int(input("Enter no1:"))
    n2=int(input("Enter no2:"))
    def add(self):
        res=self.n1+self.n2
        print("Add:",res)
    def sub(self):
        res=self.n1-self.n2
        print("sub:",res)
    def mul(self):
        res=self.n1*self.n2
        print("Mul:",res)
    def div(self):
        res=self.n1/self.n2
        print("Div:",res)
    def mod(self):
        res=self.n1%self.n2
        print("Mod:",res)
ob=op()
ob.add()
ob.sub()
ob.mul()
ob.div()
ob.mod()
