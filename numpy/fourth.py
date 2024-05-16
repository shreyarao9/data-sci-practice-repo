import numpy as np

a=np.eye(4,dtype=int)
b=np.full((4,4),4)
product=np.multiply(a,b)
print(f'Product: \n{product}',end='\n\n')

arr=np.array([1,2,3,4,5])
print(f'Array: {arr}')
print(f'Mean: {np.mean(arr)}')
print(f'Sum: {np.sum(arr)}')
print(f'After multiplication by 2: {arr*2}')