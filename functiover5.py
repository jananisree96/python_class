#Function overload:

from multipledispatch import dispatch
class A:
    @dispatch(int,int)
    def s(a,b):
        c=a*b
        print("Result:",c)
    @dispatch()
    def s():
        print("This is function overloading sample program")
    @dispatch(int,str,int)
    def s(a,b,c):
        print("Roll:",a)
        print("Name:",b)
        print("Age:",c)
ob=A
ob.s()
ob.s(4,5)
ob.s(1002,"Janani",22)
