#tabulate:

from tabulate import tabulate
x=[["Sree",22],["Abi",23],["Anu",27]]
y=["Sno","Name","Age"]
z=[1,2,3]
print(tabulate(x,headers=y,tablefmt="grid",showindex=z))
