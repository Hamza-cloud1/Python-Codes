list1=['a','b',['c',['e','f',['g','h'],'i'],'j'],'k','l']
sublist=['l','m','n']
list1[2][1][2].extend(sublist)
print(list1)
