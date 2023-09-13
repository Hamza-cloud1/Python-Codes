emails='hamza@gmail.com,maham@gmail.com,muneeb@hotmail.com,abdullah@yahoo.com'
new=list(emails.split())
for i in new:
    if '.com' in i:
        print(i)
