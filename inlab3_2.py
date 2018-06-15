A=[]
B=[]
C=[]
E=[]
n=int(input())
k=1
for i in range(0,n):
    x=int(input())
    A.append(x)
for i in range(1,n):
    for j in range(1,A[i]+1):
        if A[0]%j==0 and A[i]%j==0:
            k=j
    C=C+[(k,A[i])]
D=tuple(C)
D=sorted(D)
print(A[0])
for i in range(0,len(D)):
    print(D[i][1])
