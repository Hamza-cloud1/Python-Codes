string='hamza is engineer in programmer'
vowels='AEIOUaeiou'
count=0
for i in string:
    if i in vowels:
        count+=1
print('vowels: ',count)
