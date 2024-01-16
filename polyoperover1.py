#operator overload:

class sam:
    def __init__(self, x):
        self.x = x
        print("x value:", self.x)

    def __add__(self, y):
        self.z = self.x + y.x
        return self.z

    def __sub__(self, a):
        self.c = self.x - a.x
        return self.c

    def __mul__(self, a):
        self.d = self.c * a.x
        return self.d

    def __truediv__(self, a):
        self.e = self.x / a.x
        return self.e

    def __pow__(self, a):
        self.f = self.c ** a.x
        return self.f

# Create instances of sam
x = sam(10)
y = sam(5)

# Perform operations
print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x ** y)  # Exponentiation
