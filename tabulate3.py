#tabulate:

from tabulate import tabulate
a=[["Janani","B.com(CA)"],["Kiruthiga","B.sc(CS)"],["Sree","B.com(CA)"]]
b=["Sno","Name","Course"]
print(tabulate(a,headers=b,tablefmt='grid',showindex=True))
