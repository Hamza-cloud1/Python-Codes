cost=int(input('enter cost price:'))
sell_price=int(input('enter selling price:'))
if (sell_price-cost)>0:
    amount=sell_price-cost
    print('it is profit by:',amount)
else:
    amount=sell_price-cost
    print('it is loss',amount)
