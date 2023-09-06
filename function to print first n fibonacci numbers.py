n=int(input('enter a number:'))
def fibonacci(n):
    num1=0
    num2=1
    for i in range(1,n+1):
        num3=num1+num2
        num1=num2
        num2=num3
        print(num3,end=' ')
fibonacci(n)
