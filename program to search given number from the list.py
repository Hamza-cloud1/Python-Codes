list=[1,2,3,4,5,6,7,8,9,10]
number=int(input('enter number:'))
for i in list:
    if number==i:
        print(number,':exist')
        break
else:
    print('not found')
