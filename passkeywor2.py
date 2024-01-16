#pass keyword:

class A1:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def process(self):
        c=self.a+self.b
        print("Add:",c)
        c=self.a-self.b
        print("Sub:",c)
        c=self.a*self.b
        print("Mul:",c)
        c=self.a/self.b
        print("Div:",c)
    def print(self):
        print("Welcome this is pass keyword example program")
        print("Pass keyword is nothing but it's funtion calling...")
class A2(A1):
    pass
ob=A2(60,20)
ob.process()
ob.print()
