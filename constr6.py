#constructor:

class person:
    def __init__ (self,name,age,address,degree):
        self.name=name
        self.age=age
        self.address=address
        self.degree=degree
ob=person("Janani",22,"Mdu","B.com(CA)")
print("Name:",ob.name)
print("Age:",ob.age)
print("Address:",ob.address)
print("Degree:",ob.degree)
