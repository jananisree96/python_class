#odd and even numbers using loop methods:
a=["13579","24680"]
o=[]
e=[]
x=input("Enter your value:")
for i in x:
    if i in a[0]:
        e.append(i)
    elif i in a[1]:
            o.append(i)
print("odd num:",o)
print("Even num:",e)
