#Get the shape of an array:

import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)  #It's use to find row and column

#Reshaping array:

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(4,3)
print(newarr)


#Iterating arrays:

import numpy as np
arr=np.array([1,2,3])
for i in arr:
    print(i)

#Joining numpy arrays:

import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2))
print(arr)

#Axis:

import numpy as np
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
arr=np.concatenate((arr1,arr2),axis=1)
print(arr)


