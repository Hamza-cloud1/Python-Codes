num1=int(input('enter num1:'))
num2=int(input('enter num2:'))
num1_div=[]
num2_div=[]
for i in range(1,num1+1):
    if num1%i==0:
        num1_div.append(i)
for i in range(1,num2+1):
    if num2%i==0:
        num2_div.append(i)
common_list=[]
for i in num1_div:
    for j in num2_div:
        common_list.append(i)
print('HCF:',max(common_list))
