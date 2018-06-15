import math
n=int(input())
x=[]
y=[]
max=0
for i in range(0,n):
    k=int(input())
    x.append(k)
    k1=int(input())
    y.append(k1)

a=0
b=0
c=0
e=0
d=math.sqrt((x[1]-x[0])**2+(y[1]-y[0])**2)

for i in range(0,n):
    for j in range((i+1),n):
        d1=math.sqrt((x[j]-x[i])**2+(y[j]-y[i])**2)
        if d>=d1:
            d=d1
            a=x[i]
            b=x[j]
            c=y[i]
            e=y[j]

print(d,' is the minimum distance and it is between points (',a,',',b,') and (',c,',',e,')')            
