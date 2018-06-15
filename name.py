dic={}
n=int(input('Enter the number of employees : '))
E=[]
NO=[]
T=[]
for i in range(0,n):
    x=input("Enter the name : ")
    E.append(x)
    n1=int(input('Enter the no of phone nos the person has : '))
    for g in range(0,n1):
        y=int(input('Enter the no : '))
        NO.append(y)
    dic[E[i]]=NO
    NO=[]
X=input('Enter the name to be searched : ')
for i in range(0,len(E)):
    if E[i]==X:
        print(E[i])
        F=dic[E[i]]
        print(F)
    else:
        for j in range(0,len(E)):
            for k in range(0,len(E[j])):
                if E[j][k]!=' ':
                    T.append(E[j][k])
                else:
                    if T==X:
                        print(E[i])
                        print(dic[E[i]])
                        T=[]
                        continue
                    else:
                        print('Not Valid')
        
