import numpy as np
""" 
a=np.array([1,2,3,4,5,6])
a=a.reshape(3,2)
print(a)
a=a.reshape(2,-1)
print(a)
a=a.ravel()
print(a) """


#TRANSPOSE
""" nparr=np.random.randint(10,100,(3,3))
print(nparr)
print(nparr.T) """
a=np.arange(10).reshape(5,2)
print(a)
print(a.T)