'''name=input('Enter a name: ')
age=input('Enter an age: ')
print([name,age])
'''

vowlist=[]
i=0
while i<10:
    vov=input('Enter a vowel: ')[0]
    if vov=='a' or vov=='A' or vov=='e' or vov=='E' or vov=='i' or vov=='I' or vov=='o' or vov=='O' or vov=='u' or vov=='U':
        vowlist.append(vov)
    else:
        print('Consonant, enter a vowel: ')
        i-=1
    i+=1
for ele in vowlist:
    print(ele)


'''
number=[]
for i in range(5):
    num=int(input("Enter a number: "))
    number.append(num)
print("The numbers that you entered: ",number)'''