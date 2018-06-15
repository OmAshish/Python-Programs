x=input()
y=len(x)
k=0
i=0
j=0
while i<y :
    j=i+1
    while j<y :
        if x[i]==x[j]:
            k=1
            break
        else:
            continue
        j=j+1
    i=i+1    
if k==1:
    print('Bad')
else:
    print('Good')
