#Odd and even using list method:

a=["02468","13579"]
o=[]
e=[]
x=(input("Enter Number:")
for i in x:
    if i in a[0]:
        e.append(i)
    elif i in a[1]:
        o.append(i)
print("Odd:",o)
print("Even:",e)


