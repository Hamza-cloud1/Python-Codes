n=int(input('enter a number: '))
digit_list=list(map(int,str(n)))
digit_list=digit_list[::-1]
num=int(''.join(map(str,digit_list)))
print(num)
