n=int(input('enter range:'))
count=0
i=1
odd_list=[]
while True:
    if i%2!=0:
        odd_list.append(i)
        count=count+1
    if count==n:
        break
    i=i+1
print(odd_list)
