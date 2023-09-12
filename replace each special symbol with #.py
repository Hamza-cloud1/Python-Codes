line='he is @engineer and /programmer'
import string
for i in string.punctuation:
    if i in line:
        str=line.replace(i,'#')
print(str)
