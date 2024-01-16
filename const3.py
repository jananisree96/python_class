#constructor:
class ex:
    def __init__(self):
        self.x=int(input("Enter x value:"))
        self.y=int(input("Enter y value:"))
        z=self.x*self.y
        print("Mul:",z)
    def groc(self):
        proname=input("product name:")
        qty=int(input("Qty:"))
        cost=int(input("Cost:"))
        tot=qty*cost
        print("Total:",tot)
obj=ex()
obj.groc()
