x=input()
y=len(x)
G=x.upper()
d=G[0]
if d=='Q' or d=='W' or d=='E' or d=='R' or d=='T' or d=='Y' or d=='U' or d=='I' or d=='O' or d=='P':
    for i in range(0,y):
        e=G[i]
        if e=='Q' or e=='W' or e=='E' or e=='R' or e=='T' or e=='Y' or e=='U' or e=='I' or e=='O' or e=='P':
            k=1
            continue
        else:
            k=2
            break
    if k==1:
        print('Yes')
    else:
        print('No')
elif d=='A' or d=='S' or d=='D' or d=='F' or d=='G' or d=='H' or d=='J' or d=='K' or d=='L':
    for i in range(0,y):
        e=G[i]
        if e=='A' or e=='S' or e=='D' or e=='F' or e=='G' or e=='H' or e=='J' or e=='K' or e=='L':
            k=1
            continue
        else:
            k=2
            break
    if k==1:
        print('Yes')
    else:
        print('No')
elif d=='Z' or d=='X' or d=='C' or d=='V' or d=='B' or d=='N' or d=='M':
    for i in range(0,y):
        e=G[i]
        if e=='Z' or e=='X' or e=='C' or e=='V' or e=='B' or e=='N' or e=='M':
            k=1
            continue
        else:
            k=2
            break
    if k==1:
        print('Yes')
    else:
        print('No')
else:
    print('Not a word')
