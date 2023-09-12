line='he is 21 years old and done 25 projects'
str=line.split()
new=[]
for i in str:
    if i.isdigit()==True:
        new.append(i)
print(''.join(new))
