s=int(input('No of items given by his son : '))
d=int(input('No of items given by his daughter : '))
S=[]
D=[]
C=[]
S1=[]
D1=[]
for i in range(0,s):
    x=input('Items of the son : ')
    S.append(x)
for i in range(0,d):
    x=input('Items of the duaghter : ')
    D.append(x)

t=s+d
for i in range(0,s):
    for j in range(0,d):
        if S[i]==D[j]:
            C.append(S[i])
        else:
            S1.append(S[i])
            D1.append(D[i])
    
T=C+S1+D1
print(set(T))
