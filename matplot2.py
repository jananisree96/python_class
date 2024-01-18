#matplotlib ----- 2.Pie method:

import matplotlib.pyplot as plt
import numpy as ny
x=ny.array(["House","Gold","Land","Loan"])
y=ny.array([50,20,10,20])
plt.pie(y,labels=x)
plt.show()
