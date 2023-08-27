num=int(input('enter number:'))
new=[]
if num==1:
    print('not a prime:')
else:
    for i in range(1,num+1):
        if num%i==0:
            new.append(i)
            print(new)
    if len(new)>2:
        print('its not a prime')
    else:
        print('prime number:')
