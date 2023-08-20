n=int(input('enter 4 digit number:'))
a=n%10
num=n//10
b=num%10
num2=num//10
c=num2%10
d=num2//10
if (a**4)+(b**4)+(c**4)+(d**4)==n:
    print('yes,narcissist')
else:
    print('other:')
