list1=[12,45,65,67,87,55,66,56,87,89,99]
liat2=[45,76,7,8,6,5,55,76,4,55,87,34,65]
list3=[]
for i in list1[1::2]:
    list3.append(i)
for i in liat2[0::2]:
    list3.append(i)
print(list3)
