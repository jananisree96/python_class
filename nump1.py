#Numpy Array slicing:
#1.start:end 2.start:end:step

import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr[1:5])


#2.start:end:step

import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr[1:5:2])


#Datatypes in numpy:

import numpy as np
arr=np.array([1,2,3,4])
print(arr.dtype)

#Numpy array copy vs view:
#Copy:
print("Copy")
import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.copy()
arr[0]=42
print(arr)
print(x)

#View:
print("View")
import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.view()
arr[0]=42
print(arr)
print(x)


