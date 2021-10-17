import os
img='img.png'
bs=os.path.splitext(img)[0]
os.rename(img,bs+'.py')
exec(open("img.py").read())
img='img.py'
bs=os.path.splitext(img)[0]
os.rename(img,bs+'.png')