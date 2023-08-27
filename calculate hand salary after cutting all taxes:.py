salary=int(input('enter salary:'))
if salary in range(500000,1000000):
    salary=salary-salary*0.01
elif salary in range(1100000,2000000):
    salary=salary-salary*0.2
elif salary>2000000:
    salary=salary-salary*0.3
else:
    print('no tax:')
print('salary after tax cutting:',salary)
hra=salary-salary*0.10
da=salary-salary*0.05
pf=salary-salary*0.03
remain=salary-(hra+da+pf)
print('after cutting all taxes:',remain)
