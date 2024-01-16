#pass keyword:

class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def pr1(self):
        print("Name:",self.a)
        print("Age:",self.b)
class B(A):
    pass
ob=B("Janani",22)
ob.pr1()
