s1=input()
m1=1
def Wor(s1):
    s1.lower()
    a=b=c=d=e=f=g=h=0
    i=j=k=l=m=n=o=p=0
    q=s=r=t=u=v=w=x=0
    y=z=0
    for i1 in range(0,len(s1)):
        if s1[i1]=='a':
            a=a+1
        elif s1[i1]=='b':
            b=b+1
        elif s1[i1]=='c':
            c=c+1
        elif s1[i1]=='d':
            d=d+1
        elif s1[i1]=='e':
            e=e+1
        elif s1[i1]=='f':
            f=f+1
        elif s1[i1]=='g':
            g=g+1
        elif s1[i1]=='h':
            h=h+1
        elif s1[i1]=='i':
            i=i+1
        elif s1[i1]=='j':
            j=j+1
        elif s1[i1]=='k':
            k=k+1
        elif s1[i1]=='l':
            l=l+1
        elif s1[i1]=='m':
            m=m+1
        elif s1[i1]=='n':
            n=n+1
        elif s1[i1]=='o':
            o=o+1
        elif s1[i1]=='p':
            p=p+1
        elif s1[i1]=='q':
            q=q+1
        elif s1[i1]=='r':
            r=r+1
        elif s1[i1]=='s':
            s=s+1
        elif s1[i1]=='t':
            t=t+1
        elif s1[i1]=='u':
            u=u+1
        elif s1[i1]=='v':
            v=v+1
        elif s1[i1]=='w':
           w=w+1
        elif s1[i1]=='x':
            x=x+1
        elif s1[i1]=='y':
            y=y+1
        elif s1[i1]=='z':
            z=z+1
        else:
            continue
    if a>=1 and b>=1 and c>=1 and d>=1 and e>=1 and f>=1 and g>=1 and h>=1 and i>=1 and j>=1 and k>=1 and l>=1 and m>=1 and n>=1 and o>=1 and p>=1 and q>=1 and r>=1 and s>=1 and t>=1 and u>=1 and v>=1 and w>=1 and x>=1 and y>=1 and z>=1:
        k1=1
        return(k1)
    else:
        k1=0
        return(k1)
if Wor(s1)==m1:
    print('Pangram')
else:
    print('Not pangram')
