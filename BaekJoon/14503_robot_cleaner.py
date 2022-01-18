import copy
N,M=map(int,input().split())
cleaner_location_x,cleaner_location_y,start_direction=map(int,input().split())

matrix=[]
for i in range(N):
    tmp=list(map(int,input().split()))
    matrix.append(tmp)

visit=copy.deepcopy(matrix)

for i in range(len(matrix)):
    for k in range(len(matrix[0])):
        if matrix[i][k]==1:
            visit[i][k]=True
        else:
            visit[i][k]=False


def move(location_x,location_y,direction):
    if visit[location_x][location_y]==False:
        visit[location_x][location_y]=True
    # else:
    if direction==0:
        if visit[location_x][location_y-1]==False:
            direction=3
            location_y=location_y-1
            return location_x, location_y, direction, 1

        elif visit[location_x+1][location_y]==False:
            direction=2
            location_x=location_x+1
            return location_x, location_y, direction, 1

        elif visit[location_x][location_y+1]==False:
            direction=1
            location_y=location_y+1
            return location_x, location_y, direction, 1

        elif visit[location_x-1][location_y]==False:
            direction=0
            location_x=location_x-1
            return location_x, location_y, direction, 1

        elif matrix[location_x+1][location_y]==0:
            location_x=location_x+1
            return location_x, location_y, direction, 0

        else:
            return location_x, location_y, -1, -1

    if direction==1:
        if visit[location_x-1][location_y]==False:
            direction=0
            location_x=location_x-1
            return location_x, location_y, direction, 1

        elif visit[location_x][location_y-1]==False:
            direction=3
            location_y=location_y-1
            return location_x, location_y, direction, 1

        elif visit[location_x+1][location_y]==False:
            direction=2
            location_x=location_x+1
            return location_x, location_y, direction, 1

        elif visit[location_x][location_y+1]==False:
            direction=1
            location_y=location_y+1
            return location_x, location_y, direction, 1

        elif matrix[location_x][location_y-1]==0:
            location_y=location_y-1
            return location_x, location_y, direction, 0

        else:
            return location_x, location_y, -1, -1          

    if direction==2:
        if visit[location_x][location_y+1]==False:
            direction=1
            location_y=location_y+1
            return location_x, location_y, direction, 1

        elif visit[location_x-1][location_y]==False:
            direction=0
            location_x=location_x-1
            return location_x, location_y, direction, 1

        elif visit[location_x][location_y-1]==False:
            direction=3
            location_y=location_y-1
            return location_x, location_y, direction, 1

        elif visit[location_x+1][location_y]==False:
            direction=2
            location_x=location_x+1
            return location_x, location_y, direction, 1

        elif matrix[location_x-1][location_y]==0:
            location_x=location_x-1
            return location_x, location_y, direction, 0

        else:
            return location_x, location_y, -1, -1

    if direction==3:
        if visit[location_x+1][location_y]==False:
            direction=2
            location_x=location_x+1
            return location_x, location_y, direction, 1

        elif visit[location_x][location_y+1]==False:
            direction=1
            location_y=location_y+1
            return location_x, location_y, direction, 1

        elif visit[location_x-1][location_y]==False:
            direction=0
            location_x=location_x-1
            return location_x, location_y, direction, 1

        elif visit[location_x][location_y-1]==False:
            direction=3
            location_y=location_y-1
            return location_x, location_y, direction, 1

        elif matrix[location_x][location_y+1]==0:
            location_y=location_y+1
            return location_x, location_y, direction, 0
            
        else:
            return location_x, location_y, -1, -1            


t=0
while start_direction != -1:
    cleaner_location_x, cleaner_location_y, start_direction, work= move(cleaner_location_x,cleaner_location_y,start_direction)
    if work ==1:
        t=t+1


print(t+1)