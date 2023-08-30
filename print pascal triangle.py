n=int(input('enter a number:'))
list=[]
for i in range(0,n):
    temp=[]
    for j in range(0,i+1):
        if j==0 or j==i:
            temp.append(1)
        else:
            temp.append(list[i-1][j]+list[i-1][j-1])
    list.append(temp)
for i in range(n):
    for j in range(0,n-i-1):
        print(' ',end=' ')
    for j in range(0,i+1):
        print(list[i][j],end=' ')
    print()
