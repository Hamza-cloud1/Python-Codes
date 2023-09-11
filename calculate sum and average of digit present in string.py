line=input('enter a line: ')
def sum_avg(line):
    total=0
    count=0
    str=list(line)
    for i in str:
        if i.isdigit()==True:
            total+=int(i)
            count+=1
    print('total=',total)
    print('average=',round(total/count,2))
sum_avg(line)    
