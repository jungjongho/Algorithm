from copy import deepcopy

count_list=[]



def check(x,y,matrix):
    try:
        if matrix[x][y]==0:
            return 0
        else:
            matrix[x][y]=0
            try:
                if matrix[x-1][y]==0 and matrix[x+1][y]==0 and matrix[x][y-1]==0 and matrix[x][y+1]==0:
                    return 1
                check(x-1,y,matrix)
                check(x,y+1,matrix)
                check(x+1,y,matrix)
                check(x,y-1,matrix)
                return 1
                
            except:
                check(x-1,y,matrix)
                check(x,y+1,matrix)
                check(x+1,y,matrix)
                check(x,y-1,matrix)
                return 1
    except:
        return 0


T=int(input())



for i in range(T):
    M,N,K=map(int, input().split())
    count=0
    land=[]
    for i in range(N):
        land.append([0]*M)

    for i in range(K):
        x,y=map(int,input().split())
        land[y][x]=1

    land_copy=deepcopy(land)

    for i in land:
        print(i)

    for i in range(M):
        for j in range(N):
            count = count + check(i,j,land_copy)

    print(count)
    count_list.append(count)

for i in count_list:
    print(i)