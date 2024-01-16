#Function overload:

from multipledispatch import dispatch

class sam:
    @dispatch(str, int, str)
    def ex1(a, b, c):
        print("Name:", a)
        print("Age:", b)
        print("Address:", c)

    @dispatch(int, int)
    def ex1(a, b):
        c = a * b
        print("c value:", c)

    @dispatch()
    def ex1():
        print("Welcome to all")

obj = sam()
obj.ex1()
obj.ex1("sree", 22, "Madurai")
obj.ex1(4,5)
