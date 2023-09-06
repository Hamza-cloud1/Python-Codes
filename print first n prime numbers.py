num=int(input('enter a number:'))
list=[]
for i in range(1,num+1):
    if num%i==0:
        list.append(i)
if len(list)>2:
    print('it is not a prime number')
else:
    print('it is a prime number')
