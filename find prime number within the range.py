def prime(n):
    if n<=0:
        return False
    else:
        list=[]
        for i in range(1,n+1):
            if n%i==0:
                list.append(i)
        if len(list)<=2:
            return True
        else:
            return False
num1=int(input('enter number1:'))
num2=int(input('enter number2:'))
for i in range(num1,num2+1):
    if prime(i)==True:
        print(i ,end=' ')
