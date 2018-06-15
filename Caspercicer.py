x=input()
dno=int(input())
y=len(x)
X=""
d=0
for i in range(0,y):
    z=ord(x[i])
    e=z+dno
    if e>122:
        f=e-122
        g=97+f
        d=g
        X=X+chr(g)
    else:
        X=X+chr(e)
print(X)
