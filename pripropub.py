#private,protected using class and object:

class x:
    def _sample(self):
        print("Welcome Everyone")
        print("Student Bio and marklist")
class y:
    def __init__(self):
        name=input("Enter your Name:")
        age=int(input("Enter Age:"))
        address=input("Enter Address:")
    def __marks(self):
        m1=int(input("Mark1:"))
        m2=int(input("Mark2:"))
        m3=int(input("Mark3:"))
        tot=m1+m2+m3
        print("Total:",tot)
        avg=tot/3
        print("Average:",avg)
    def call(self):
        self.__marks()
ob=x()
ob._sample()
ob1=y()
ob1.call()
