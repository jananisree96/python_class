#Splitting numpy arrays:

import numpy as np
arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,3)
print(newarr)

#Numpy searching arrays:

#Find the index where the values is 4:

import numpy as np
arr=np.array([1,2,3,4,5,4,4])
x=np.where(arr==4)
print(x)

#Sorting arrays:

import numpy as np
arr=np.array(['banana','cherry','apple'])
print(np.sort(arr))

#numpy filter array:

import numpy as np
arr=np.array([41,42,43,44])
x=arr[[True,False,True,False]]
print(x)
