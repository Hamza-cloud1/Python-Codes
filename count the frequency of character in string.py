a=input('enter a line:')
b=input('enter a character')
count=0
for i in a:
    if i in b:
        count+=1
print('frequency of searched character is:',count,' times')
