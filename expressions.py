n=int(input())
m=int(input())
m=m+1
n=n+1
A=[]
B=[]
for i in range (0,n) :
    C=int(input())
    A=A.append(C)

for i in range (0,m) :
    D=int(input())
    B=B.append(D)

if m>=n:
    c=m-n
    for i in range(0,c):
        A.insert(0,0)
if m<=n:
    c=n-m
    for i in range(0,c):
        B.insert(0,0)
G=[]
if m>=n:
    for i in range(0,m):
        f=A[i]+B[i]
        G=G.append(f)
        
print(G)
