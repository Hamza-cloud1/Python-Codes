roll_num=[3,4,6,7,8,9,12,43,5,7,8]
sample={'qasim':1,
        'ali':5,
        'hamza':2,
        'haris':43}
roll_num=[item for item in roll_num if item in sample.values()]
print(roll_num)
