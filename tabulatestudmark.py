#Studentmarklist using tabulate module:

from tabulate import tabulate
n=[]
tam=[]
eng=[]
mat=[]
sci=[]
soc=[]
tot=[]
for i in range(5):
    name=input("Student Name:")
    n.append(name)
    t=int(input("Tamil:"))
    tam.append(t)
    e=int(input("English:"))
    eng.append(e)
    m=int(input("Maths:"))
    mat.append(m)
    s=int(input("Science:"))
    sci.append(s)
    ss=int(input("Social:"))
    soc.append(ss)
    total=t+e+m+s+ss
    tot.append(total)
x=[]
h=["Sno","Name","Tamil","English","Maths","science","Social","Total"]
for i in range(5):
    y=[n[i],tam[i],eng[i],mat[i],sci[i],soc[i],tot[i]]
    x.append(y)
print(tabulate(x,headers=h,tablefmt="simple",showindex="always"))


    
    
