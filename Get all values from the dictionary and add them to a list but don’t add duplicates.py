serial={
    'qasim':1,
        'ali':5,
        'hamza':2,
        'haris':43,
        'ahmed':5
}
new=[]
for value in serial.values():
    if value not in new:
        new.append(value)
print(new)
