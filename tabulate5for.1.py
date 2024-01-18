#Multiple students name and age get and using tabulate module:

from tabulate import tabulate
n=[]
a=[]
for i in range(3):
    name=input("Enter Name:")
    n.append(name)
    age=int(input("Enter Age:"))
    a.append(age)
y=[]    
for i in range(3):
    x=[n[i],a[i]]
    y.append(x)
print(tabulate(y,tablefmt="Plain"))
    
