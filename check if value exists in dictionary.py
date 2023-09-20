dict={'a':100,'b':200,'c':300,'d':400}
n=int(input('enter a number:'))
if n in dict.values():
    print('{} present in dict:'.format(n))
else:
    print('not')
