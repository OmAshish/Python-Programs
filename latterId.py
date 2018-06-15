a=input().rstrip()
b=input().rstrip()
c=input().rstrip()
a1=len(a)
b1=len(b)
c1=len(c)
l1=[]
l2=[]
l3=[]
l4=[]
q=0
q1=0
for i in range(0,a1):
    for j in range(0,b1):
        for k in range(0,c1):
            if a[i]==b[j] and a[i]==c[k] and b[j]==c[k]:
                l1.append(a[i])
            if a[i]==b[j] and b[j]!=c[k]:
                l2.append(a[i])
            if a[i]!=b[j] and a[i]!=c[k]:
                l3.append(a[i])
            l4.append(a[i])
            l4.append(b[j])
            l4.append(c[k])    
print(set(l1))
print(list(set(l2)))
print(list(set(l3)))
print(list(set(l4)))

        
