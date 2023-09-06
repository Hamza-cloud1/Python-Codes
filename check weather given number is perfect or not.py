from functools import reduce
list=[]
n=int(input('enter a number: '))
def perfect(n):
    for i in range(1,n):
        if n%i==0:
            list.append(i)
    result=reduce(lambda x,y: x+y,list)
    if n==result:
        print(n, ' is perfect number')
    else:
        print('other')
perfect(n)
