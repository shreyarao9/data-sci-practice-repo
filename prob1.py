for i in range(9,20):
    a=(i-9)
    a=(a*2)+1
    print(f'{a}/{i*i*i +1}')

asc=97
num=7
count=0
while(asc<123):
    print(f'{chr(asc)}/{num}')
    num=num+(2*count)+1
    asc+=1
    count+=1