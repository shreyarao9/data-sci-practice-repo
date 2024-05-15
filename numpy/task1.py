import numpy as np

emptyarr=np.empty((3,3),dtype=int)
fullarr=np.full((4,4),2)
print('Empty array: ',emptyarr)
print('Full array: \n',fullarr,end="\n\n")

arr=np.array([1,2,3,4,3,3],dtype=int)
print('Array: ',arr)
n=np.bincount(arr)
print('Element with the highest frequency in the array: ',np.argmax(n),end="\n\n")

a=np.random.randint(10,50,(3,3))
b=np.random.randint(10,50,(3,3))
print(f'Array A: \n{a}')
print(f'Array B: \n{b}')
print('Comparing A and B: \n',np.greater(a,b),end="\n\n")

specific_val_array=np.full((3,3),9)
print('Empty array added with specific value array: \n',emptyarr+specific_val_array)