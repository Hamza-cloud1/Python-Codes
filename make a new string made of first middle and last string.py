str1=input('enter word1: ')
str2=input('enter word2: ')
def mix(str1,str2):
    l1=len(str1)//2
    a=str1[0]
    b=str2[l1]
    c=str1[-1]
    l2=len(str2)//2
    x=str2[0]
    y=str2[l2]
    z=str2[-1]
    print('mix string=',a,z,b,y,c,z)
mix(str1,str2)
