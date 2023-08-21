p=int(input('enter amount:'))
r=int(input('enter rate interest:'))
t=int(input('enter time in months:'))
si=(p*r*t)/100
print('simple interest:',si)
due_amount=p+si
print('due amount:',due_amount)
