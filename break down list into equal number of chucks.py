list1=[1,2,3,4,5,6,7,8,9,10]
chunck=3
b=[list1[i:i+chunck] for i in range(0,len(list1),chunck)]
print(b)
