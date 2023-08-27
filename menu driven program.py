choice=int(input("""user menu:
press 1 for cm to ft:
press 2 for kl to miles:
press 3 for usd to pkr:
press 4 for exit:"""))
if choice==1:
    cm=float(input('enter value in cm:'))
    ft=cm/30
    print(ft,':feet')
elif choice==2:
    km=float(input('enter value in km:'))
    miles=km/1.64
    print(miles,':miles')
elif choice==3:
    usd=float(input('enter value in usd:'))
    pkr=usd*285
    print(pkr,'pkr')
else:
    print('exit:')
