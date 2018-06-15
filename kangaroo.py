j=0
s1=input()
s2=input()
m=''
for i in range(0,len(s1)):
        if s1[i]==s2[j]:
            m=m+s1[i]
            j=j+1
if m==s2:
    print('True')
else:
    print('False')
