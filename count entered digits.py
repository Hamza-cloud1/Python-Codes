n=input('enter a number:')
l=list(n)
count=0
while count<len(l):
    for i in l:
        count+=1
print(count)
