n=int(input('enter a number:'))
factorial=1
if n<0:
    print('not valid:')
elif n==0:
    print('fictorial of 0 always 1')
else:
    for i in range(1,n+1):
        factorial=factorial*i
    print(factorial)
