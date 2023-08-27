head=int(input('enter number of heads:'))
legs=int(input('enter number of legs:'))
if head/legs==0.25:
    number_of_dogs=legs/4
    print(f'there are {round(number_of_dogs)} dogs:')
elif head/legs==0.5:
    number_of_chicken=legs/2
    print(f'there are {round(number_of_chicken)} chickens')
else:
    print('invalid:')
