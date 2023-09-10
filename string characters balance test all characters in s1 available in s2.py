str1=input('enter string 1: ')
str2=input('enter string 2: ')
def bal(str1,str2):
    count=0
    for i in str1:
        if i in str2:
            count+=1
    if len(str1)==count:
        print('balanced string:')
    else:
        print('unbalanced')
bal(str1,str2)
