#single inheritance:
class A:
    def __init__(self):
        self.name=input("Enter name:")
        self.height=int(input("Enter the height:"))
        self.width=int(input("Enter the width:"))
class B(A):
    def result(self):
        tot=self.height*self.width
        print("Name:",self.name)
        print("Height:",self.height)
        print("width:",self.width)
        print("Total:",tot)
x=B()
x.result()
    
