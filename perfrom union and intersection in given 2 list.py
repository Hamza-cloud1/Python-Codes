l1=[1,2,3,4,5]
l2=[3,4,5,7,8,1,2,4]
uni=[]
inter=[]
for i in l1:
    if i in l2:
        inter.append(i)
print('intersaction: ',inter)
for i in l1:
    if i not in uni:
        uni.append(i)
for i in l2:
    if i not in uni:
        uni.append(i)
print('union: ',uni)
