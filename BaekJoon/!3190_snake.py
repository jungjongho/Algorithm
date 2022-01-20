N=int(input())
K=int(input())
apple=[]
for i in range(K):
    k=list(map(int,input().split()))
    apple.append(k)
L=int(input())
direction=[]
for i in range(L):
    l,m=input().split()
    direction.append([int(l),m])

matrix=[ [0] * N for _ in range(N) ]

for i in apple:
    matrix[i[0]-1][i[1]-1]=1

matrix[0][0]=3


time=0
snake_location_x=0
snake_location_y=0
orientation=10000002
#direction%4=2 -> right   : D-> -1
#direction%4=1 -> down    : L-> +1


def move_right(matrix,snake_location_x,snake_location_y,direction,num,orientation,time, p):
    try:

        for j in range(num):
            time = time +1
            for i in matrix:
                print(i)
            print('=='*40,'right') 
            if matrix[snake_location_x][snake_location_y+1]==0:
                matrix[snake_location_x][snake_location_y+1]=3
                matrix[snake_location_x][snake_location_y]=0
                snake_location_y=snake_location_y+1

            elif matrix[snake_location_x][snake_location_y+1]==1:
                matrix[snake_location_x][snake_location_y+1]=3
                matrix[snake_location_x][snake_location_y]=2
                snake_location_y= snake_location_y+1

            elif matrix[snake_location_x][snake_location_y+1]==2:
                return matrix, snake_location_x, snake_location_y,orientation,time, -1
                
        if direction=='D':
            orientation= orientation-1
            return matrix, snake_location_x, snake_location_y,orientation,time, 0

        elif direction=='L':
            orientation += 1
            return matrix, snake_location_x, snake_location_y,orientation,time, 0
    except:
        return matrix, snake_location_x, snake_location_y,orientation,time, -1


def move_left(matrix,snake_location_x,snake_location_y,direction,num,orientation,time,p):
    try:

        for j in range(num):

            time = time +1
            for i in matrix:
                print(i)
            print('=='*40,'left') 
            if matrix[snake_location_x][snake_location_y-1]==0:
                matrix[snake_location_x][snake_location_y-1]=3
                matrix[snake_location_x][snake_location_y]=0
                snake_location_y=snake_location_y-1

            elif matrix[snake_location_x][snake_location_y-1]==1:
                matrix[snake_location_x][snake_location_y-1]=3
                matrix[snake_location_x][snake_location_y]=2
                snake_location_y= snake_location_y-1

            elif matrix[snake_location_x][snake_location_y-1]==2:
                return matrix, snake_location_x, snake_location_y,orientation,time, -1
                
        if direction=='D':
            orientation= orientation-1
            return matrix, snake_location_x, snake_location_y,orientation,time, 0

        elif direction=='L':
            orientation += 1
            return matrix, snake_location_x, snake_location_y,orientation,time ,0
    except:
        return matrix, snake_location_x, snake_location_y,orientation,time, -1

def move_up(matrix,snake_location_x,snake_location_y,direction,num,orientation,time,p):
    try:

        for j in range(num):
            time = time +1
            for i in matrix:
                print(i)

            print('=='*40,'up')    
            if matrix[snake_location_x-1][snake_location_y]==0:
                matrix[snake_location_x-1][snake_location_y]=3
                matrix[snake_location_x-1][snake_location_y]=0
                snake_location_x=snake_location_x-1

            elif matrix[snake_location_x-1][snake_location_y]==1:
                matrix[snake_location_x-1][snake_location_y]=3
                matrix[snake_location_x-1][snake_location_y]=2
                snake_location_x= snake_location_x-1

            elif matrix[snake_location_x-1][snake_location_y]==2:
                return matrix, snake_location_x, snake_location_y,orientation,time, -1
                
        if direction=='D':
            orientation= orientation-1
            return matrix, snake_location_x, snake_location_y,orientation,time, 0

        elif direction=='L':
            orientation += 1
            return matrix, snake_location_x, snake_location_y,orientation,time ,0 
    except:
        return matrix, snake_location_x, snake_location_y,orientation,time, -1

def move_down(matrix,snake_location_x,snake_location_y,direction,num,orientation,time,p):
    try:
        for j in range(num):
            time = time +1
            for i in matrix:
                print(i)
            print('=='*40,'down') 
            if matrix[snake_location_x+1][snake_location_y]==0:
                matrix[snake_location_x+1][snake_location_y]=3
                matrix[snake_location_x][snake_location_y]=0
                snake_location_x=snake_location_x+1

            elif matrix[snake_location_x+1][snake_location_y]==1:
                matrix[snake_location_x+1][snake_location_y]=3
                matrix[snake_location_x-1][snake_location_y]=2
                snake_location_x= snake_location_x+1

            elif matrix[snake_location_x+1][snake_location_y]==2:
                return matrix, snake_location_x, snake_location_y,orientation,time, -1
                
        if direction=='D':
            orientation= orientation-1
            return matrix, snake_location_x, snake_location_y,orientation,time, 0

        elif direction=='L':
            orientation += 1
            return matrix, snake_location_x, snake_location_y,orientation,time, 0
    except:
        return matrix, snake_location_x, snake_location_y,orientation,time, -1

p=0


for i in range(L):
    print('=='*30)
    if orientation%4==2:
        matrix, snake_location_x, snake_location_y, orientation, time,p =move_right(matrix,snake_location_x,snake_location_y,direction[i][1],direction[i][0],orientation,time,p)
    elif orientation%4==1:
        matrix, snake_location_x, snake_location_y, orientation, time,p =move_down(matrix,snake_location_x,snake_location_y,direction[i][1],direction[i][0],orientation,time,p)
    elif orientation%4==0:
        matrix, snake_location_x, snake_location_y, orientation, time,p =move_left(matrix,snake_location_x,snake_location_y,direction[i][1],direction[i][0],orientation,time,p)
    elif orientation%4==3:
        matrix, snake_location_x, snake_location_y, orientation, time,p =move_up(matrix,snake_location_x,snake_location_y,direction[i][1],direction[i][0],orientation,time,p)
    
    if p==-1:
        break
print(time)