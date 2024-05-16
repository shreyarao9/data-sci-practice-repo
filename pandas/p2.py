import pandas as pd

data={
    'A':[1,2,3],
    'B':[4,5,6],
    'C':[7,8,9]
}
df=pd.DataFrame(data,index=['X','Y','Z'])

#use loc to access a specific row and column by label
value_loc=df.loc['Y','C']
print('Value using loc: ',value_loc)

#use iloc to access a specific row amd column by index
value_iloc=df.iloc[0,1]
print('Value using iloc: ',value_iloc)