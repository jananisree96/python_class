#private,protected using class and object:

class A:
    def __init__(self):
        self.x=int(input("Enter Age:"))
    def __display(self):
        print("Age:",self.x)
    def dis(self):
        self.__display()
class B:
    def _sam(self):
        print("This is protected function")
a=A()
a.dis()
b=B()
b._sam()
