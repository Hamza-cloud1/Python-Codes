line=input('enter a line: ')
def lowup(line):
    new=[]
    sma=list(line.lower())
    cap=list(line.upper())
    for i in line:
        if i in sma:
            new.append(i)
    for i in line:
        if i in cap:
            new.append(i)
    result=' '.join(new)
    print(result)
lowup(line)
