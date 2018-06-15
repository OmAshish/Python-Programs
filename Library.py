r=input()
n=int(input())
x=[n]
k=0
for i in range(0,n):
    x[i]=int(input())
for i in range(0,n):
    for j in range((i+1),n):
        if x[i]==x[j]:
            continue
        else:
            print(x[i])
for i in range(0,n):
    if x[i]==r:
        k=1
        break
if k==1:
    print('Found')
else:
    print('Not Found')
