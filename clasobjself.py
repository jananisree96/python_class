#class and object using self method:
class op:
    no1=int(input("Enter num1:"))
    no2=int(input("Enter num2:"))
    def add(self):
        res=self.no1+self.no2
        print("Add:",res)
    def sub(self):
        res=self.no1-self.no2
        print("Sub:",res)
    def mul(self):
        res=self.no1*self.no2
        print("Mul:",res)
    def div(self):
        res=self.no1/self.no2
        print("Div:",res)
    def mod(self):
        res=self.no1%self.no2
        print("Mod:",res)
ob=op()
ob.add()
ob.sub()
ob.mul()
ob.div()
ob.mod()
