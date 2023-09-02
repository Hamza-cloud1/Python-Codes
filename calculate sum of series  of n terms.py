n=int(input('enter range:'))
num=int(input('enter a number:'))
result=0
for i in range(1,n+1):
    y=str(num)*i
    z=int(''.join(y))
    result+=z
print(result)
