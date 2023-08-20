n=int(input('enter 3 digits:'))
a=n%10
num=n//10
b=num%10
c=num//10
if (a**3)+(b**3)+(c**3)==n:
    print('yes,armstrong')
else:
    print('other')
