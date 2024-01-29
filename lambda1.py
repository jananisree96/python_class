#lambda:

a=lambda n:n*n
n=int(input("Enter n value:"))
print(a(n))

print("-----Lambda Declaration-----")
x=lambda a:a+10
print(x(25))

x=lambda a,b,c:a*b+c
print(x(5,6,10))
print()


print("----Using lambda in function----")
def myfun(n):
    return lambda S:S+n
d=myfun(10)
print(d(100))
print()

print("----lAMBDA KEYWORD----")
A=[11,15,-40,60,18,9,3,12]
B=list(filter(lambda x:(x%2==0),A))
C=list(map(lambda x:x*2,A))
D=list(map(lambda x:pow(x,3),A))
print(B)
print(C)
print(D)

