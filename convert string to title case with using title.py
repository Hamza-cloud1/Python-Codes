title=input('enter title:')
def cap(s):
    s=title.split()
    r=' '
    for i in s:
        r=r+i.capitalize()+' '
    print(r)
cap(title)
