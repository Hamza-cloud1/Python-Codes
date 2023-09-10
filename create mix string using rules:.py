str1=input('enter word1:')
str2=input('enter word2:')
def mix(str1,str2):
    a=str1[0]
    b=str1[len(str1)//2]
    c=str1[-1]
    x=str2[0]
    y=str2[len(str2)//2]
    z=str2[-1]
    result=' '.join([a,z,b,x,c,y])
    print('result=',result)
mix(str1,str2)
