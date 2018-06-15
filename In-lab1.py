c=()
d=()
a0=int(input())
a1=int(input())
b0=int(input())
b1=int(input())
h=sqrt((a0-b0)^2 + (a1-b1)^2)
c0=b0
c1=b1-(((h*h)-(b0-c0)*(b0-c0))**0.5)
c1=int(c1)
d0=a0
d1=c1
c=(c0,c1)
d=(d0,d1)
H=format(h,'.2f')
print(c)
print(d)
print(H)
