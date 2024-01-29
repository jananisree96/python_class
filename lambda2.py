#Lambda

print("Finding Odd and Even using lambda:")
x=[11,2,4,22,5,6,77,9,0,8,1]
y=list(filter(lambda i:(i%2==0),x))
z=list(filter(lambda i:(i%2==1),x))
print("X value:",x)
print("Even number:",y)
print("Odd number:",z)


print("Using math fun in lambda")
from math import *
a=[2,3,4,5,6,7,8]
a1=[2,9,16,25,36,49]
b=list(map(lambda i:i*2,a))
c=list(map(lambda i:pow(i,3),a))
d=list(map(lambda i:sqrt(i),a1))
print("a value:",a)
print("Mul:",b)
print("Pow:",c)
print("a1 value:",a1)
print("sqrt of a1:",d)


