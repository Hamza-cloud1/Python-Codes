n=int(input('enter 4 digits:'))
a=n%10
num1=n//10
b=num1%10
num2=num1//10
c=num2%10
d=num2//10
rev=a*1000+b*100+c*10+d
print(rev)
if(n==rev):
    print(True)
else:
    print(False)
