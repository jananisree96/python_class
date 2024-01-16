#calendar and math modules using class and object:

class package_modules:
    print("Calendar and math module")
    print("------------------------")
    def calendar_module(self):
        print("calendar module")
        print("----------------")
        print("2024 year calendar")
        print("-------------------")
        import calendar
        print(calendar.calendar(2024))
        print("---------------------")
        print("Month of june-2024")
        print("---------------------")
        print(calendar.month(2024,4))
        print("---------------------")
        print("Month range of Nov-2023")
        print(calendar.monthrange(2024,6))
        print("-------------------------")
    def math_module(self):
        print("Math modules")
        print("------------")
        import math
        print("Pie value:",math.pi)
        print("Enumerate value:",math.e)
        print("Absolute value:(-23)-",math.fabs(-23))
        print("Ceil value:(23.433)-",math.ceil(23.433))
        print("Floor value:(52.344)-",math.floor(52.344))
        no1=int(input("Enter no1:"))
        no2=int(input("Enter no2:"))
        c=math.pow(no1,no2)
        print("Power:",c)
        print("Sin value of no1:",math.sin(no1))
ob=package_modules()
ob.calendar_module()
ob.math_module()

