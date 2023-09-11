line=['my','name','','hamza',None,'','is']
for i in line:
    if i=='' or i==None:
        line.remove(i)
print(line)
