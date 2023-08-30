n=int(input('enter a number:'))
total=0
count=0
avg=0
while True:
    if n!=0:
        total=total+n
        count+=1
        avg=total/count
        n=int(input('enter another number:'))
    else:
        print('thank you:')
        break
print('sum=',total)
print('average:',avg)
