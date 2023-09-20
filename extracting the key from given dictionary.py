dict1={'name':'ahmed',
       'age':19,
       'weight':67,
       'city':'rwp'}
keys=['name','city']
result=dict()
for k in keys:
    result.update({k:dict1[k]})
print(result)
