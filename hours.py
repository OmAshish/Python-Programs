x=input()
y=x[8:len(x)]
z=""
a2=''
a=x[0:2]
b=x[3:5]
c=x[6:8]
a1=int(a)
b1=int(b)
c1=int(c)
if y=='AM':
    d=a1+12
    if d==24:
        a2='00'
    else:
        a2=str(a1)
if y=='PM':
    a1=a1+12
    a2=str(a1)
        
        
if a1>=0 and a1<=23:
    if b1>=0 and b1<=59:
        if c1>=0 and c1<=59:
            z=a2+':'+b+':'+c
            print(z)
