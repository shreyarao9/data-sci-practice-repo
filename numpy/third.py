import numpy as np

#CONCATENATE
""" a=np.zeros((2,4),dtype=int)
b=np.ones((2,4),dtype=int)

print(np.concatenate((a,b)))
 """

#LINSPACE
""" eqspace=np.linspace(10,100,6,dtype=int)
print(eqspace)

#syntax for equal value array
#variable_name=np.arrange(start_range,end_range,diff
eqSpaceAr=np.arange(10,30,6) """

#IDENTITY MATRIX
""" a=np.eye(4,dtype=int)
print(a)  """

#CREATING RANDOM ARRAYS
""" arr=np.random.randint(10,100,(3,3))
print(arr) """

#SPECIFIC VALUE ARRAY
z=np.full((4,4),4)
print(z)
