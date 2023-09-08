name='hamza-ahmed'
l=len(name)
if l%2==0:
    print('not possible')
else:
    c=l//2
    x=name[c-1]
    y=name[c]
    z=name[c+1]
    result=' '.join([x,y,z])
    print(result)
