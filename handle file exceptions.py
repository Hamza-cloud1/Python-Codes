file=r'C:\Users\ha298\Documents\bse203006.txt'
try:
    with open(file) as fp:
        content=fp.read()
        print(content)
except FileNotFoundError:
    print(f'file {file} not found:')
