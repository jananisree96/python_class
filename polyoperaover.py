class binary:
    def __init__(self, a):
        self.a = a

    def __add__(self, b):
        self.c = self.a + b.a
        return self.c

    def __sub__(self, c):
        self.d = self.c - self.a
        return self.d

    def __mul__(self, d):
        self.f = self.d * self.a
        return self.f

    def __truediv__(self, f):
        self.g = self.f / self.d
        return self.g

    def __pow__(self, b):
        self.j = self.a ** b.a
        return self.j


x = binary(10)
y = binary(5)

print("x + y:", x + y)
print("x - y:", x - y)
print("x * y:", x * y)
print("x / y:", x / y)
print("x ** y:", x ** y)
