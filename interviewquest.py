#PYTHON PROGRAM TO REMOVE DUPLICATE ELEMENT FROM A LIST
# PYTHON PROG TO COUNT THE OCCURRENCE OF AN ITEM IN A LIST
n=int(input('input the list size: '))
print('input list elements: ')
lis=[]
for i in range(n):
    lis.append(int(input()))
print(f'Input list: {lis}')
lis2=[lis[0]]
for i in range(len(lis)):
    count=0
    for j in range(len(lis2)):
        if lis[i]==lis2[j]:
            count+=1
    if count==0:
        lis2.append(lis[i])
print(f'List after removing duplicates: {lis2}')


for i in range(len(lis2)):
    count=0
    for j in range(len(lis)):
        if lis2[i]==lis[j]:
            count+=1
    print(f'Element {lis2[i]} appears in the list {count} times')