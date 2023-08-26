n=int(input('enter amount:'))
a=10000
b=10000
c=n-(a+b)
tax=0
if n<=a:
    tax=0
elif n>a and n<20000:
    tax=b*0.1
else:
    tax=(b*0.1)+(c*0.2)
print(tax)
