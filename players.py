dict={}
N=[]
E=[]
n=int(input('No of players in each team : '))
m=int(input('No of teams : '))
for i in range(0,m):
    z=input('Enter the team''s name: ')
    E.append(z)
    for j in range(0,n):
        u=input('Enter the player''s name : ')
        N.append(u)
    dict[E[i]]=N
    N=[]
F=input('Enter the team name u want to see the players : ')
for i in range(0,m):
    if F==E[i]:
        print(dict[E[i]])
