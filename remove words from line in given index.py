word=input('enter a word: ')
n=int(input('enter index: '))
def remove(word,n):
    x=len(str(word))
    p=list(word)
    for i in p:
        if n<=x:
            z=word[n:]
    print(z)
remove(word,n)
