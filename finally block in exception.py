num1=int(input('enter num1:'))
num2=int(input('enter num2:'))
try:
    result=num1/num2
except ZeroDivisionError:
    print('math error:')
finally:
    print('result',result)
    print('you got it:')
