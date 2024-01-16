#function overloading:
from multipledispatch import dispatch
class A:
    @dispatch()
    def sam():
        print("Function overloading...")
    @dispatch(int,int)        
    def sam(a,b):
        c=a*b
        print("Multiple value:",c)
    @dispatch(int,int,int)        
    def sam(a,b,c):
        d=a*b+c
        print("Result:",d)
    @dispatch(str,int)        
    def sam(a,b):
        print("Name:",a)
        print("Age:",b)
ob=A
ob.sam()        
ob.sam(5,2,4)
ob.sam(6,5)
ob.sam("Janani",22)

