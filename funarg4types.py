'''function arg-
1.required arg,
2.keyword arg,
3.default arg
4.variable lenghth arg'''

#Required arg:
def aa(a,b,c):
    print("Roll:",a)
    print("Name:",b)
    print("Address:",c)
aa(121,"Janani","Mdu")

#keyword arg:
def bb(x,y,z):
    print("Name:",x)
    print("Age:",y)
    print("Blood group:",z)
bb(x="Janani",y=22,z="O+")

#Default arg:
def cc(name="ssss",course="MCA"):
    print("Hi i'm {},i have completed {} course".format(name,course))
cc("Janani","B.com(CA)")
cc()    #default arg

#Variable length arg:
def favfood(*food):
    for i in food:
        print("My fav food is:",i)
favfood("Biriyani","Chicken friedrice","Noodles")    

    
