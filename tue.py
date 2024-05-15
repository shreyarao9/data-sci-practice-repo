'''
vow=input('Enter a vowel: ')[0]
if vow=='a' or vow=='A':
    print('A has been entered')
elif vow=='e' or vow=='E':
    print('E has been entered')
elif vow=='i' or vow=='I':
    print('I has been entered')
elif vow=='o' or vow=='O':
    print('O has been entered')
elif vow=='u' or vow=='U':
    print('U has been entered')
else:
    print('Consonant entered')
'''

'''
lis=[]
for i in range(5):
    lis.append(input('Enter a string: '))
print(lis)
'''

""" lst=['abc','xyz','pqr']
for ele in lst:
    print(ele) """

""" lst1=[1,2,3,4,5,6,7,8,9,10]
for ele in lst1:
    if ele%2==0: print(ele) """

""" str=input('Enter a sentence: ')
str=str.strip()
count=1
for i in str:
    if i==' ': count+=1
print(f'No of words= {count}') """

""" lst=[]
i=0
while(i<5):
    lst.append(int(input('Enter a num: ')))
    i=i+1
print(f'Length of list= {len(lst)}')
lst.sort()
print(f'Sorted list: {lst}') """

""" varr=(12,)
print(varr[-1:0]) """

atup=(21,34,64,76,87,32,94,33,51)
print(sorted(atup))
print(len(atup))
num=int(input('Enter a number: '))
print(f'Is {num} present in tuple? {num in atup}')