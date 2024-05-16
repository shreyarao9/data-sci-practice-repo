import pandas as pd

data={
    'Name': ['Soo','Skillan','Sasha'],
    'Age':[19,20,25],
    'City':['Bangalore','Mangalore','Mumbai']
}

df=pd.DataFrame(data)
print(f'Data Frame: \n{df}')

filtered_df=df[df['Age']<24]
print(f'Filtered Dataframe: \n{filtered_df}')