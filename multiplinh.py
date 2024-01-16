#multiple inheritance:
class get:
    print("Employee details:")
    def __init__ (self):
        self.roll=int(input("Emp rollno:"))
        self.name=input("Emp name:")
        self.gender=input("Emp gender:")
        self.age=int(input("Emp age:"))
        self.qual=input("Qualification:")
        self.add=input("Emp add:")
class wages:
    def salary(self):
        self.pos=input("Emp position:")
        self.sal=int(input("Emp sal:"))
class A(get,wages):
    def print(self):
        print("Emp rollno:",self.roll)
        print("Emp name:",self.name)
        print("Gender:",self.gender)
        print("Age:",self.age)
        print("Qualification:",self.qual)
        print("Address:",self.add)
        print("Position:",self.pos)
        print("Salary:",self.sal)
ob=A()
ob.salary()
ob.print()
