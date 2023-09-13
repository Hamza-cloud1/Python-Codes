list=[1,2,3,4,4,4,4,4,9,6,6,5,6,7,8,9,10]
count=dict()
for i in list:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
