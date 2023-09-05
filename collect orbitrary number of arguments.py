def pizza(size,*topping):/
    print(f'making {size} pizza: ')
    print('toppings: ')
    for i in topping:
        print(i)
pizza('large','bbq','sauce','vegis')
