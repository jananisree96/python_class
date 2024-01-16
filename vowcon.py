#vowels and consonents using list methods:
a=["aeiouAEIOU","bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ","0123456789"]
v=[]
c=[]
n=[]
s=[]
mail=input("Enter your email id:")
for i in mail:
    if i in a[0]:
        v.append(i)
    elif i in a[1]:
        c.append(i)
    elif i in a[2]:
        n.append(i)
    else:
        s.append(i)
print("No of vowels:",v)
print("No of consonents:",c)
print("No of numeric:",n)
print("No of speacial character:",s)
