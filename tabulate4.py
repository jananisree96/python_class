#tabulate:

from tabulate import tabulate
a=[["Apple",50],["Banana",20],["Orange",60]]
b=["Productname","Price"]
print(tabulate(a,headers=b,tablefmt="Plain",showindex=False))
