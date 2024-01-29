import matplotlib.pyplot as plt
import numpy as ny
a=ny.array(["Apple","Banana","Strawberry","Gova"])
b=ny.array([40,25,30,75])
c=ny.array(["Boys","Girls","Transgender"])
d=ny.array([40,45,15])
plt.pie(b,labels=a)
plt.show()
plt.plot(c,d)
plt.show()
plt.bar(a,b)
plt.show()
