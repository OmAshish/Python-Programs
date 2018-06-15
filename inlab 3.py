from fractions import gcd
n =int(input())
k=int(input())
l=[]
for i in range(0,n-1):
    h=int(input())
    l.append(h)
l2=[]
for i in l:
    l2=l2+[gcd(k,i)]
l3=[]
for x,y in zip(l2,l):
    l3=l3+[[x,y]]
l3.sort()
l3[0:0]=[[0,k]]
for i in l3:
    print(i[1], end=',')
