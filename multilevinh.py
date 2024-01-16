#Multileval inheritance:
class A:
    def get_a(self):
        rollno=int(input("Enter Rollno:"))
        name=input("Enter Name:")
        age=int(input("Enter Age:"))
        address=input("Enter Address:")
class B(A):
    def get_b(self):
        m1=int(input("Mark1:"))
        m2=int(input("Mark2:"))
        m3=int(input("Mark3:"))
        m4=int(input("Mark4:"))
        m5=int(input("Mark5:"))
        self.tot=m1+m2+m3+m4+m5
        print("Total:",self.tot)
        self.avg=self.tot/5
        print("Average:",self.avg)
class C(B):
    def get_c(self):
        if(self.avg>=100):
            print("A Grade")
        elif(self.avg>=85):
            print("B Grade")
        elif(self.avg>=65):
            print("C Grade")
        else:
            print("D Grade")
        if(self.tot>350):
            print("Pass")
        else:
            print("Fail")
obj=C()
obj.get_a()
obj.get_b()
obj.get_c()
