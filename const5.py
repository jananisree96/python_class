#constructor:
class sam:
    def __init__(self):
        self.a=int(input("Enter A value:"))
        self.b=int(input("Enter B value:"))
        self.add=self.a+self.b
        self.sub=self.a-self.b
        self.mul=self.a*self.b
        self.div=self.a/self.b
        self.mod=self.a%self.b
        self.expo=self.a**self.b
        self.flodiv=self.a//self.b
    def display(self):
        print("Add:",self.add)
        print("Sub:",self.sub)
        print("Mul:",self.mul)
        print("Div:",self.div)
        print("Mod:",self.mod)
        print("Exponentiation:",self.expo)
        print("Floor div:",self.flodiv)
ob=sam()
ob.display()
