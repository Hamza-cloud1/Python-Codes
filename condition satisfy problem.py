num=[1000,50,150,23,43,23,12,654,765,342]
for i in num:
    if i>500:
        break
    elif i>150:
        continue
    else:
        if i%5==0:
            print(i)
