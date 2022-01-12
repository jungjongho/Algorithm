from itertools import combinations

N=int(input())
matrix=[]
for i in range(N):
    number=list(map(int,input().split()))
    matrix.append(number)
    
N=int(N)
A=int(N/2)

team1=[]
team2=[]
total=set(range(1,N+1))


it=combinations(range(1,N+1),A)
for num in it:
    team1.append(list(num))
    team2.append(list(total-set(num)))
    
    
point1=[]
point2=[]

for i in team1:
    point=combinations(i,2)
    pt=0
    for k in point:
        # print(k)
        # print(matrix[k[0]-1][k[1]-1]+matrix[k[1]-1][k[0]-1])
        pt=pt+matrix[k[0]-1][k[1]-1]+matrix[k[1]-1][k[0]-1]

    point1.append(pt)
    
for i in team2:
    point=combinations(i,2)
    pt=0
    for k in point:
        # print(k)
        # print(matrix[k[0]-1][k[1]-1]+matrix[k[1]-1][k[0]-1])
        pt=pt+matrix[k[0]-1][k[1]-1]+matrix[k[1]-1][k[0]-1]

    point2.append(pt)
    
point_sub=[]
for i,j in zip(point1,point2):
    point_sub.append(abs(i-j))

print(min(point_sub))