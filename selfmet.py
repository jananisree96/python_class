#self method:

class sam:
    a=10
    b=20
    def ex1(self):
        self.c=self.a*self.b
        print("welcome..")
    def dis(self):
        print("Mul:",self.c)
x=sam()
x.ex1()
x.dis()
