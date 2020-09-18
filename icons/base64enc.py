import os,sys,base64

res={}
for name in ('n0.png','n1.png','n2.png','c0.png','c1.png','c2.png'):
    with open(name,'rb') as picture:
        res[name]=base64.b64encode(picture.read())

with open('out.txt','w') as file:
    file.write(str(res))