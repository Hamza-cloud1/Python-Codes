set_1={1,2,3,4,5,6,7,8,9,10}
set_2={1,2,3,6,9}
print('first set in subset of second set: ',set_1.issubset(set_2))
print('second set is subset of first set: ',set_2.issubset(set_1))
print('first set is super set of second set',set_1.issuperset(set_2))
print('secondt set is super set of first set',set_2.issuperset(set_1))
if set_1.issubset(set_2):
    set_1.clear()
if set_2.issubset(set_1):
    set_2.clear()
print('set 1: ',set_1)
print('set 2: ',set_2)
