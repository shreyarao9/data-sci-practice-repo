import pandas as pd

data= {'Name': ['Soo','Skillan','Sasha'],
       'Age':[19,20,25],
       'City':['Bengaluru','Udupi','Mumbai']}

df=pd.DataFrame(data)
#df.insert(2,"Timezone",['IST','IST','IST'],True) #check the difference when you run only this, vs creating df2 and using assign()
df2=df.assign(Timezone=['IST','IST','IST'])

print(df2)