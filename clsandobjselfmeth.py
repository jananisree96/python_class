#class and obj using self method:

class op:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    def add(self):
        res=self.a+self.b
        print("Add:",res)
    def sub(self):
        res=self.a-self.b
        print("Sub:",res)
    def mul(self):
        res=self.a*self.b
        print("Mul:",res)
    def div(self):
        res=self.a/self.b
        print("Div:",res)
    def mod(self):
        res=self.a%self.b
        print("Mod:",res)
ob=op()
ob.add()
ob.sub()
ob.mul()
ob.div()
ob.mod()
