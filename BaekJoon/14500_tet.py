N,M=map(int,input().split())
matrix=[]
for i in range(N):
    tmp=list(map(int,input().split()))
    matrix.append(tmp)


def L(matrix,location_x,location_y):
    
    point_list=[]

    try: # case:1
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x][location_y+1]
        point=point +matrix[location_x][location_y+2]
        point=point +matrix[location_x+1][location_y]
        point_list.append(point)
    except IndexError:
        pass

    try: #case:2
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x][location_y-1]
        point=point +matrix[location_x+1][location_y]
        point=point +matrix[location_x+2][location_y]
        point_list.append(point)
    except IndexError:
        pass

    try: #case:3
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x][location_y-1]
        point=point +matrix[location_x][location_y-2]
        point=point +matrix[location_x-1][location_y]
        point_list.append(point)
    except IndexError:
        pass

    try: #case:4
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x][location_y+1]
        point=point +matrix[location_x-1][location_y]
        point=point +matrix[location_x-2][location_y]
        point_list.append(point)
    except IndexError:
        pass

    try: #case:5
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x][location_y-1]
        point=point +matrix[location_x][location_y-2]
        point=point +matrix[location_x+1][location_y]
        point_list.append(point)
    except IndexError:
        pass

    try: #case:6
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x][location_y-1]
        point=point +matrix[location_x-2][location_y]
        point=point +matrix[location_x-1][location_y]
        point_list.append(point)
    except IndexError:
        pass

    try: #case:7
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x][location_y+1]
        point=point +matrix[location_x][location_y+2]
        point=point +matrix[location_x-1][location_y]
        point_list.append(point)
    except IndexError:
        pass

    try: #case:8
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x][location_y+1]
        point=point +matrix[location_x+1][location_y]
        point=point +matrix[location_x+2][location_y]
        point_list.append(point)
    except IndexError:
        pass



    try:
        return max(point_list)
    except:
        return 0


def square(matrix,location_x,location_y):
    
    point_list=[]

    try: # case:1
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x][location_y+1]
        point=point +matrix[location_x+1][location_y]
        point=point +matrix[location_x+1][location_y+1]
        point_list.append(point)
    except IndexError:
        pass

    try: # case:2
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x][location_y-1]
        point=point +matrix[location_x-1][location_y]
        point=point +matrix[location_x-1][location_y-1]
        point_list.append(point)
    except IndexError:
        pass
    
    try: # case:3
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x][location_y+1]
        point=point +matrix[location_x-1][location_y]
        point=point +matrix[location_x-1][location_y+1]
        point_list.append(point)
    except IndexError:
        pass

    try: # case:4
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x][location_y-1]
        point=point +matrix[location_x+1][location_y]
        point=point +matrix[location_x+1][location_y-1]
        point_list.append(point)
    except IndexError:
        pass

    try:
        return max(point_list)
    except:
        return 0



def I(matrix,location_x,location_y):
    point_list=[]
    try: # case:1
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x][location_y-1]
        point=point +matrix[location_x][location_y-2]
        point=point +matrix[location_x][location_y-3]
        point_list.append(point)
    except IndexError:
        pass
    
    try: # case:2
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x][location_y+1]
        point=point +matrix[location_x][location_y+2]
        point=point +matrix[location_x][location_y+3]
        point_list.append(point)
    except IndexError:
        pass

    try: # case:3
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x-1][location_y]
        point=point +matrix[location_x-2][location_y]
        point=point +matrix[location_x-3][location_y]
        point_list.append(point)
    except IndexError:
        pass

    try: # case:4
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x+1][location_y]
        point=point +matrix[location_x+2][location_y]
        point=point +matrix[location_x+3][location_y]
        point_list.append(point)
    except IndexError:
        pass

    try:
        return max(point_list)
    except:
        return 0



def Z(matrix,location_x,location_y):
    point_list=[]

    try: # case:1
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x][location_y+1]
        point=point +matrix[location_x-1][location_y+1]
        point=point +matrix[location_x-1][location_y+2]
        point_list.append(point)
    except IndexError:
        pass

    try: # case:2
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x+1][location_y]
        point=point +matrix[location_x+1][location_y+1]
        point=point +matrix[location_x+2][location_y+1]
        point_list.append(point)
    except IndexError:
        pass

    try: # case:3
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x][location_y+1]
        point=point +matrix[location_x+1][location_y+1]
        point=point +matrix[location_x+1][location_y+2]
        point_list.append(point)
    except IndexError:
        pass

    try: # case:4
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x+1][location_y]
        point=point +matrix[location_x+1][location_y-1]
        point=point +matrix[location_x+2][location_y-1]
        point_list.append(point)
    except IndexError:
        pass
    
    try:
        return max(point_list)
    except:
        return 0


def fuck(matrix,location_x,location_y):
    point_list=[]

    try: # case:1
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x][location_y+1]
        point=point +matrix[location_x+1][location_y]
        point=point +matrix[location_x-1][location_y]
        point_list.append(point)
    except IndexError:
        pass

    try: # case:2
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x+1][location_y]
        point=point +matrix[location_x][location_y+1]
        point=point +matrix[location_x][location_y-1]
        point_list.append(point)
    except IndexError:
        pass

    try: # case:3
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x][location_y-1]
        point=point +matrix[location_x+1][location_y]
        point=point +matrix[location_x-1][location_y]
        point_list.append(point)
    except IndexError:
        pass

    try: # case:4
        point =0 
        point=point +matrix[location_x][location_y]
        point=point +matrix[location_x-1][location_y]
        point=point +matrix[location_x][location_y-1]
        point=point +matrix[location_x][location_y+1]
        point_list.append(point)
    except IndexError:
        pass
    
    try:
        return max(point_list)
    except:
        return 0


test=[]
for i in range(N):
    for j in range(M):
        point_arr=[]
        point_arr.append(L(matrix,i,j))
        point_arr.append(fuck(matrix,i,j))
        point_arr.append(I(matrix,i,j))
        point_arr.append(Z(matrix,i,j))
        point_arr.append(square(matrix,i,j))
        test.append(max(point_arr))

print(max(test))