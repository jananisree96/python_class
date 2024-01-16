#task-4 types of arg:
#Required Argument:
def bio(name,age,dob,address):
    print("Name:",name)
    print("Age:",age)
    print("DOB:",dob)
    print("Address:",address)
#keyword argument:    
def qual(sname,clgname,course,yop):
    print("School:",sname)
    print("College name:",clgname)
    print("Course:",course)
    print("Yop:",yop)
#Default argument:    
def intro(name="Janani" ,age=22,address="Madurai"):
    print("Hi everyone my name is {},my age is {},I am from {}".format(name,age,address))
#variable length argument:    
def hob(*hobby):
    for i in hobby:
        print("My hobby is:",i)
#function calling:        
bio("Janani",22,"9.6.2001","Mdu")
qual(yop=2021,course="B.com(CA)",sname="sou.g.hr.sec.school",clgname="Ambika clg")
intro()
hob("Cooking","Listening songs")

