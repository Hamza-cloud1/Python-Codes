file=r'C:\Users\ha298\Documents\bse203006.txt'
with open(file) as file_obj:
    for line in file_obj:
        print(line.rstrip())
