r=int(input())
c=int(input())
x=[[0 for i in range(c)] for j in range(r)]
z=0
n=0
for i in range(0,r):
    for j in range(0,c):
        t=int(input())
        x[i][j]=t
for i in range(0,r):
    for j in range(0,c):
        if x[i][j]==0:
            z=z+1
        else:
            n=n+1
if r>0 and c>0:
    if z>=n:
        print('Sparse')
    else:
        print('Not sparse')
else:
    print('Invalid input')
