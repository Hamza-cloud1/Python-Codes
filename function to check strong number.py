n=int(input('enter a number:'))
result=0
def fact(n):
    total=1
    for i in range(1,n+1):
        total*=i
    return total
for i in str(n):
    x=fact(int(i))
    result+=x
if n==result:
    print(n,' is strong number:')
else:
    print('other')
