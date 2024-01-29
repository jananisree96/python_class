class Bio:
    print("Multilevel Inheritance")

    def __init__(self):
        self.n = input("Enter Name:")
        self.a = int(input("Enter Age:"))
        self.add = input("Enter Address:")

class A(Bio):
    def mark(self):
        self.m1 = int(input("Mark1:"))
        self.m2 = int(input("Mark2:"))
        self.m3 = int(input("Mark3:"))
        self.m4 = int(input("Mark4:"))
        self.m5 = int(input("Mark5:"))
        self.tot = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
        print("Total:", self.tot)
        self.avg = self.tot / 5
        print("Average:", self.avg)

class B(A):
    def res(self):
        if self.avg >= 90:
            print("A Grade")
        elif 75 <= self.avg < 90:
            print("B Grade")
        elif 65 <= self.avg < 75:
            print("C Grade")
        elif 50 <= self.avg < 65:
            print("D Grade")
        else:
            print("Poor performance")

ob = B()
ob.mark()
ob.res()
