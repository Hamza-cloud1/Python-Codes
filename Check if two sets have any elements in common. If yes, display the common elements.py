set1={2,3,4,5,6,7}
set2={8,9,0,1,2,3}
if set1.isdisjoint(set2):
    print('no common elements:')
else:
    print(set1.intersection(set2))
