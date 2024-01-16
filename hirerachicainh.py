#Hirearchical inheritance:
class showroom:
    def __init__(self):
        print("Welcome to sree motors")
        print("Available Models:scootypep,Royal Enfield,pulser")
class scootypep(showroom):
    def scooty(self):
        print("Thank you for choosing scootypep")
        print("Model:2023")
        price=160000
        dis=price*5/100
        fa=price-dis
        print("Actual price:",price)
        print("Discount:",dis)
        print("Final Amt:",fa)
class royalenfield(showroom):
    def re(self):
        print("Thank you for choosing Royal Enfield")
        print("Model:2023")
        price=250000
        dis=price*5/100
        fa=price-dis
        print("Actual price:",price)
        print("Discount:",dis)
        print("Final Amt:",fa)
class pulser(showroom):
    def puls(self):
        print("Thank you for choosing Pulser")
        print("Model:2022")
        price=270000
        dis=price*5/100
        fa=price-dis
        print("Actual price:",price)
        print("Discount:",dis)
        print("Final Amt:",fa)
print("\n1.for scootypep\n 2.for Royalenfield\n 3.for pulser\n")
ch=int(input("Enter your choice:"))
if(ch==1):
    ob=scootypep()
    ob.scooty()
elif(ch==2):
    ob1=royalenfield()
    ob1.re()
elif(ch==3):
    ob2=pulser()
    ob2.puls()
else:
    print("Invalid selection")
