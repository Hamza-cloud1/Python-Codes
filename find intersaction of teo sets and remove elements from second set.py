set1={45,65,67,78,76,56,34,23,4,5,6}
set2={67,78,56,23,4,5,6,45,65,67,23,54,3}
intersection=set1.intersection(set2)
print('intersaction: ',intersection)
for i in intersection:
    set2.remove(i)
print(set2)
