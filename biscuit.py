n=int(input())
dict={}
N=[]
O=[]
l=[]
q=[]
p=[]
for i in range(0,n):
    x=input()
    l.append(x)
for i in range(0,n):
    y=int(input())
    q.append(y)
    z=int(input())
    p.append(z)
    O=[q,p]
    N.append(O)
    dict[l[i]]=N

m=int(input())
M=[]
Q=[]
for i in range(0,m):
    x=input()
    M.append(x)
    y=int(input())
    Q.append(y)

c=0

for i in range(0,n):
    for j in range(0,m):
        if l[i]==M[j]:
            if Q[j]<=q[i]:
                c=c+Q[j]*p[i]
            else:
                continue
print(c)

for i in range(0,n):
    for j in range(0,m):
        if l[i]==M[j]:
            q[i]=q[i]-Q[j]
            O=[q,p]
            N.append(O)
            dict[l[i]]=N[i]

print(dict)
