n=int(input())
k=1
def A(n):
    s=str(n)
    y=len(s)
    print(y)
    p=n**2
    d=p%(10**y)
    return(d)
    
if A(n)==n:
    print('Automorphic')
else:
    print('Not automorphic')
