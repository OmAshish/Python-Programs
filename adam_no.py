n=int(input())
n1=0
c=0
p=n**2
def f1(n):
    s=str(n)
    s1=s[::-1]
    n1=int(s1)
    p1=n1**2
    s=str(p1)
    s1=s[::-1]
    p2=int(s1)
    return(p2)
if p==f1(n):
    print('Adam number')
else:
    print('Not Adam Number')
