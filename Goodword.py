x=input()
y=len(x)
k=0
for i in range(0,y):
    for j in range((i+1),y):
        if x[i]==x[j]:
            k=1
            break
        else:
            continue
if k==1:
    print('Bad')
else:
    print('Good')
