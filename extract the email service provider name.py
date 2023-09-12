emails=['hamza@gmail.com','maham@gmail.com','muneeb@hotmail.com','abdullah@yahoo.com']
for i in emails:
    i=i.replace('@','.').split('.')
    print(i[1])
