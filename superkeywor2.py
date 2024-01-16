#super() keyword:

class stud:
    def __init__(self,rollno,name):
        self.a=rollno
        self.b=name
class mark(stud):
    def __init__(self,rollno,name,m1,m2,m3):
        super().__init__(rollno,name)
        self.c=m1
        self.d=m2
        self.e=m3
    def display(self):
        print("Rollno:",self.a)
        print("Name:",self.b)
        print("Mark1:",self.c)
        print("Mark2:",self.d)
        print("Mark3:",self.e)
class final(mark):
    def __init__(self,rollno,name,m1,m2,m3,address):
        super().__init__(rollno,name,m1,m2,m3)
        self.ad=address
    def display2(self):
        tot=self.c+self.d+self.e
        print("Total:",tot)
        avg=tot/3
        print("Average:",avg)
        print("Address:",self.ad)
ob=final(152,"Diya",90,85,75,"Madurai")
ob.display()
ob.display2()

