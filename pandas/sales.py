import pandas as pd

sales_data={
    'Product_name':['Lamp','Pen','Battery','Keychain'],
    'Selling price':[200,10,10,20],
    'Cost price':[150,8,7,17],
    'Sales':[1900,20032,15395,11827]
}

s_df=pd.DataFrame(sales_data)
print(s_df)

filter_df=s_df[s_df['Sales']>10000]
print(f'Filtered Dataframe: \n{filter_df}')
