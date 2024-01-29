class shop:
    print("Hirearchical Inheritance")
    def __init__(self):
        print("Welcome Js Mall")
class f(shop):
    def fr(self):
        print("\n1.Apple\n 2.Banana\n")
        n=int(input("Enter your choice:"))
        if(n==1):
            print("You are selected Apple")
            qty=int(input("How many kg do u want?"))
            a=50
            tot=a*qty
            print("Total:",tot)
        elif(n==2):
            print("You are selected Banana")
            qty=int(input("How many banana do u want?"))
            b=10
            tot=b*qty
            print("Total:",tot)
        else:
            print("Invalid option")
class v(shop):
    def ve(self):
        print("\n 1.Potato\n 2.Carrot\n")
        n=int(input("Enter your choice:"))
        if(n==1):
            print("You are selected potato")
            qty=int(input("How many kg do u want?"))
            p=30
            tot=p*qty
            print("Total:",tot)
        elif(n==2):
            print("You are selected carrot")
            qty=int(input("How many kg do u want?"))
            c=20
            tot=c*qty
            print("Total:",tot)
        else:
            print("Invalid option")
class i(shop):
    def ic(self):
        print("\n 1.vennila\n 2.Butterscotch\n")
        n=int(input("Enter your choice:"))
        if(n==1):
            print("You are selected vennila")
            qty=int(input("How many do u want?"))
            v=25
            tot=v*qty
            print("Total:",tot)
        elif(n==2):
            print("You are selected butterscotch")
            qty=int(input("How many do u want?"))
            bs=40
            tot=bs*qty
            print("Total:",tot)
        else:
            print("Invalid option")
            
print("Available products:1.Fruits,2.vegitables,3.ice cream")
n=int(input("How many orders do u want?"))
for j in range(n):
    ch=int(input("Enter your choice:"))
    if(ch==1):
        ob=f()
        ob.fr()
    elif(ch==2):    
        ob1=v()
        ob1.ve()
    elif(ch==3):    
        ob2=i()
        ob2.ic()
    else:
        print("Error")
