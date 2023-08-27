temp=int(input('enter temperature:'))
humidity=int(input('enter humidity:'))
if temp>=30 and humidity>=90:
    print('hot and humid')
elif temp>=30 and humidity<90:
    print('hot')
elif temp<30 and humidity>=90:
    print('cool and humid')
else:
    print('cool')
