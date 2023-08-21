import os
size=os.stat(r'C:\Users\ha298\Documents\project.ipynb').st_size
if size==0:
    print('empty:')
else:
    print('not empty:')
