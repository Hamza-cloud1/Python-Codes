prevent crash from user input
print('enter numbers:')
print('press q for quiet')
while True:
    num1=input('enter num1:')
    if num1=='q':
        print('end')
        break
    num2=input('enter num2:')
    if num2=='q':
        print('end')
        break
    try:
        result=int(num1)/int(num2)
    except ZeroDivisionError:
        print('math error:')
    else: 
        print(result)
