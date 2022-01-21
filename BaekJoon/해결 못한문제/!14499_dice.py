import itertools 
import copy

N,M,X,Y,K=map(int,input().split())
matrix=[]

for i in range(N):
    ma=list(map(int,input().split()))
    matrix.append(ma)

direction=list(map(int,input().split()))

dice=[0,0,0,0,0,0]

dice_location_x=X
dice_location_y=Y

def move(matrix,direction,start_location_x,start_location_y,dice):

    height=N-1
    width=M-1


    if direction == 1:
        start_location_x=start_location_x
        start_location_y=start_location_y+1

        if (0>start_location_y) or (start_location_y>width):
            start_location_y=start_location_y-1
            return start_location_x, start_location_y


        tmp=dice[0]
        dice[0]=dice[5]
        dice[5]=dice[2]
        dice[2]=dice[4]
        dice[4]=tmp

        if matrix[start_location_x][start_location_y]==0:
            pass
        else:
            tmp=dice[0]
            dice[0]=matrix[start_location_x][start_location_y]
            matrix[start_location_x][start_location_y]=tmp


    if direction == 2:
        start_location_x=start_location_x
        start_location_y=start_location_y-1

        if (0>start_location_y) or (start_location_y>width):
            start_location_y=start_location_y+1
            return start_location_x, start_location_y

        tmp=dice[0]
        dice[0]=dice[4]
        dice[4]=dice[2]
        dice[2]=dice[5]
        dice[5]=tmp

        if matrix[start_location_x][start_location_y]==0:
            pass
        else:
            tmp=dice[0]
            dice[0]=matrix[start_location_x][start_location_y]
            matrix[start_location_x][start_location_y]=tmp
            
    if direction == 3:
    
        start_location_x=start_location_x-1
        start_location_y=start_location_y

        if (0>start_location_x) or (start_location_x>height):
            start_location_x=start_location_x+1
            return start_location_x, start_location_y

        tmp=dice[0]
        dice[0]=dice[1]
        dice[1]=dice[2]
        dice[2]=dice[3]
        dice[3]=tmp

        if matrix[start_location_x][start_location_y]==0:
            pass
        else:
            tmp=dice[0]
            dice[0]=matrix[start_location_x][start_location_y]
            matrix[start_location_x][start_location_y]=tmp

    if direction == 4:
        start_location_x=start_location_x+1
        start_location_y=start_location_y

        if (0>start_location_x) or (start_location_x>height):
            start_location_x=start_location_x-1
            return start_location_x, start_location_y

        tmp=dice[0]
        dice[0]=dice[3]
        dice[3]=dice[2]
        dice[2]=dice[1]
        dice[1]=tmp

        if matrix[start_location_x][start_location_y]==0:
            pass
        else:
            tmp=dice[0]
            dice[0]=matrix[start_location_x][start_location_y]
            matrix[start_location_x][start_location_y]=tmp



    print(dice[2])

    return start_location_x, start_location_y


for i in direction:
    dice_location_x, dice_location_y=move(matrix,i,dice_location_x,dice_location_y,dice)