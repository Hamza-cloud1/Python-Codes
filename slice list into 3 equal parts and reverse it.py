list=[1,2,3,4,5,6,7,8,9,10]
n=3
parts=[list[i:i+n] for i in range(0,len(list),n)]
print(parts)
