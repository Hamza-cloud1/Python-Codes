num1=int(input('enter first number:'))
num2=int(input('enter second number:'))
try:
    result=num1/num2
except ZeroDivisionError:
    print('math error:')
else:
    print('result: ',result)
