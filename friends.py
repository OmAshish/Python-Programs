n=0
ch=input()
name=''
N=0
max1=0
s='stop'
y=0
while ch!=s:
    y=len(ch)
    n=n+1
    if max1<=y:
        max1=y
        name=ch
        N=n
    print('Enter the next name : ')
    ch=input()
    
print(N,',',name,',',max1)
