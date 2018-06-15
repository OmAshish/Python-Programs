x=input()
a=x[0]
y=len(x)
cn=0
cs=0
if a.isalpha():
    if y>=8: 
        for i in range(0,y):
            if x[i]=='0' or x[i]=='1' or x[i]=='2' or x[i]=='3' or x[i]=='4' or x[i]=='5' or x[i]=='6' or x[i]=='7' or x[i]=='8' or x[i]=='9':
                cn=cn+1
            elif x[i]>='A' and x[i]<='Z':
                continue
            else:
                cs=cs+1
                
        if cn>=1 and cs>=1:
            print('Valid')
        else:
            print('Invalid')
