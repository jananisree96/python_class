#Function Argument-1.Required argument:

def sample(x,y,z):
    print("Name:",x)
    print("Age:",y)
    print("Address:",z)
sample("Janani",22,"Madurai")

#Function Argument-2.keyword argument:

def aa(a,b,c):
    print("Roll:",a)
    print("Name:",b)
    print("Age:",c)
aa(b="Janani",a=12112,c=22)    

#Function Argument-3.default argument:

def ex(name="Jana",age=22,course="B.com(CA)"):
    print("Hai I am {},my age {},I have completed {} course".format(name,age,course))
ex()    


#Function Argument-4.variable length argument:

def a1(*name):
    for i in name:
        print("My name is:",i)
a1("aa","bb","cc","dd")        

