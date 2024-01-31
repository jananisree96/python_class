#class and obj
class A:
    def __init__(self):   #constructor
        print("Welcome")
    def add(self):
        a=10
        b=20
        c=a+b
        print("Add:",c)
class B:
    def bio(self):
        n=input("Enter name:")
        a=int(input("Age:"))
    def __mark(self):       #private
        m1=int(input("Mark1:"))
        m2=int(input("Mark2:"))
        tot=m1+m2
        print("Tot:",tot)
    def call(self):   #public
        self.__mark()
class C:
    def _sam(self):     #protected
        print("This is protected")
ob=A()
ob.add()
ob1=B()
ob1.call()
ob2=C()
ob2._sam()
