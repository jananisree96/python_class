#Hybrid Inheritance:
class A:
    def det(self):
        self.name=input("Enter Name:")
        self.gender=input("Enter Gender:")
        self.age=int(input("Enter age:"))
class B(A):
    def mark(self):
        self.det()
        self.t=int(input("Tamil:"))
        self.e=int(input("English:"))
        self.m=int(input("Maths:"))
        self.s=int(input("science:"))
        self.ss=int(input("Sos_sci:"))
        self.tot=self.t+self.e+self.m+self.s+self.ss
        print("Total:",self.tot)
        self.avg=self.tot/5
        print("Avg:",self.avg)
class C:
    def games(self):
        nss=int(input("NSS:"))
        sports=int(input("Sports:"))
        self.bonus=nss+sports
        print("Bonus Marks:",self.bonus)
class D(B,C):
    def overall(self):
        print("Name:",self.name)
        print("Gender:",self.gender)
        print("Age:",self.age)
        print("Tamil:",self.t)
        print("English:",self.e)
        print("Maths:",self.m)
        print("Science:",self.s)
        print("Soc_sci:",self.ss)
        print("Total:",self.tot)
        print("Average:",self.avg)
        print("Bonus mark:",self.bonus)
        Finalsco=self.tot+self.bonus
        print("Final Score:",Finalsco)
ob=D()
ob.mark()
ob.games()
ob.overall()
