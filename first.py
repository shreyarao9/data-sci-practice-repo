'''a=8
b=5
print(a*b/a+b-a)
print(a*b/(a+b)-a)
print(a/b*a+b-a)
'''

'''
b=""
a=[34,72,69,76,76,79,32,87,79,82,76,68,34]
for i in a:
    b=b+chr(i)
print(b)
'''

for i in range(0,31,3): 
    if i%2 ==0: print(f'3 x {int(i/3)} = {i}')