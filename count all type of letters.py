line=input('enter a line: ')
def sep(line):
    l1=list(line)
    char=0
    digit=0
    special_ch=0
    for i in l1:
        if i.isalpha()==True:
            char+=1
        elif i.isdigit()==True:
            digit+=1
        else:
            special_ch+=1
    print('character=',char)
    print('digit=',digit)
    print('special=',special_ch)
sep(line)
