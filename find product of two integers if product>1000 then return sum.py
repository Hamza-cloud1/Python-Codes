num1=int(input('enter num1:'))
num2=int(input('enter num2:'))
def mul_sum_int(num1,num2):
    mul=num1*num2
    total=num1+num2
    if mul<=1000:
        print('product=',mul)
    else:
        print('sum=',total)
mul_sum_int(num1,num2)
