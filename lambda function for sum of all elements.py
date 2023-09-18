from functools import reduce
l1=[1,2,3,4,5,6]
sum=reduce(lambda x,y : x+y ,l1)
print('sum=',sum)
