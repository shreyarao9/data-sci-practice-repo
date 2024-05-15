import numpy as np
from time import process_time

pyList=[]
for i in range(1000000):
    pyList.append(i)

start_time=process_time()
pyList=[i+5 for i in range(1000000)]
end_time=process_time()
print(end_time-start_time)

pyList2=[i for i in range(1000000)]
np_arr=np.array(pyList2)
starttime2=process_time()
np_arr+=5
endtime2=process_time()
print(endtime2-starttime2)