import pandas as pd

data={
    'Kumar':[10000,1000],
    'ASR':[100000,10000],
    'Ravi':[50000,5000]
}

df=pd.DataFrame(data,index=['Salary','Expense'])
print(df)
savings=df.loc['Salary','Ravi']-df.loc['Expense','Ravi']
print(f'Ravi\'s savings: {savings}')