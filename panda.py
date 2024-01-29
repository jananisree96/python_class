#Pandas:

import pandas as pd
import numpy as np
print("--------Method 1 Declare-------")
print("--------Creating dataframes--------")
a=pd.DataFrame({'x':[35,45,55,65,75],'y':[20,30,40,50,60],'z':[2,3,4,5,6]});
print(a)

print("------creating series from array------")
info=np.array(['p','a','n','d','a','s'])
a=pd.Series(info)
print(a)

print("-----Accessing data from series with position-----")
x=pd.Series([1,2,3],index=['a','b','c'])
print(x[2])

print("------Method 2 Declare with columns------")
df = pd.DataFrame([[21,72,67.1],[23,78,69.5],[32,74,56.6],[52,54,76.2]],columns=['a','b','c'])
print("The DataFrame is :\n",df)

shape = df.shape
print("\n DataFrame Shape :",shape)
print("\n Number of Rows:", shape[0])
print("\n Number of Columns:", shape[1])

