#student marklist:
class ml:
   
    def __init__(self):
        self.name=input("Enter name:")
        self.t=int(input("Tamil:"))
        self.e=int(input("English:"))
        self.m=int(input("Maths:"))
        self.s=int(input("Science:"))
        self.ss=int(input("Soc_sci:"))
    def result(self):
        tot=self.t+self.e+self.m+self.s+self.ss
        print("Total:",tot)
        avg=tot/5
        print("Average:",avg)
n=int(input("No of students:"))
for i in range(n):
    ob=ml()
    ob.result()
