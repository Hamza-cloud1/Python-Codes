with open(r'C:\Users\ha298\Documents\empty.txt','r') as fr:
    lines=fr.readlines()
with open(r'C:\Users\ha298\Documents\empty1.txt','w') as fw:
    count=0
    for line in lines:
        if count==4:
            count+=1
            continue
        else:
            fr.write(line)
        count+=1
