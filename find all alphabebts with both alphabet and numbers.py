line='hamza007,basit111 they are programmers'
str=line.split()
new=[]
for i in str:
    for j in i:
        if j.isdigit()==True:
            if i not in new:
                new.append(i)
print(new[:])
