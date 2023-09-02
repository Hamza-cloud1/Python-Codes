n=int(input('enter a number:'))
num1=0
num2=1
for i in range(0,n):
    num3=num1+num2
    num1=num2
    num2=num3
    print(num3,end=' ')
