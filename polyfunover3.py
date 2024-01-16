#function overload:

from multipledispatch import dispatch
class A:
    @dispatch(str,int)
    def op(a,b):
        print("Name:",a)
        print("Age:",b)
    @dispatch(str,str,int,str)
    def op(c,x,y,z):
        print("Address:",c)
        print("DOB:",x)
        print("Salary:",y)
        print("Course:",z)
    @dispatch(int,int)
    def op(a,b):
        c=a+b
        print("Add:",c)
        c=a-b
        print("Sub:",c)
        c=a*b
        print("Mul:",c)
        c=a/b
        print("Div:",c)
        c=a%b
        print("Mod:",c)
    @dispatch()
    def op():
        if(True):
                print("Yes")
        else:
                print("No")
ob=A
ob.op("Janani",22)
ob.op("Madurai","09/06/2001",45000,"B.com(CA)")
ob.op(20,5)
ob.op()

