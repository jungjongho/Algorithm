from itertools import product

from itertools import chain
import copy
#python3 의경우 시간초과
#pypy3의 경우 괜찮음

#효율성의 문제를 어떻게 해결할것인지 다른사람의 코드를 보는것을 추천


N=int(input())
matrix_original=[]
for i in range(N):
    number=list(map(int,input().split()))
    matrix_original.append(number)


def game(matrix,op):
    size=len(matrix)
    
    if op=='left':
        for x in range(size): # x=[0,1,2,3]
            for k in range(size-1):
                for y in range(size-1): # y=[0,1,2]
                    if matrix[x][y]==0:
                        matrix[x][y]=matrix[x][y+1]
                        matrix[x][y+1]=0

                        # for y_tmp in range(y,size-2): # y_tmp= [y,...,2]
                        #     matrix[x][y_tmp+1]=matrix[x][y_tmp+2]

            for y in range(size-1): # y=[0,1,2]
                if matrix[x][y]==matrix[x][y+1]:
                    matrix[x][y] = matrix[x][y]*2

                    for y_tmp in range(y,size-2): # y_tmp= [y,...,2]
                        matrix[x][y_tmp+1]=matrix[x][y_tmp+2]
                    matrix[x][size-1]=0

        return matrix
        
    if op=='right':
        for x in range(size): # x=[0,1,2,3]
            for k in range(size-1):
                for y in range(size-1): # y=[0,1,2]
                    if matrix[x][(size-1)-(y)]==0:
                        matrix[x][(size-1)-(y)]=matrix[x][(size-1)-(y+1)]
                        matrix[x][(size-1)-(y+1)]=0

                    # for y_tmp in range(y,size-2): # y_tmp= [y,...,2]
                    #     matrix[x][(size-1)-(y_tmp+1)]=matrix[x][(size-1)-(y_tmp+2)]

            for y in range(size-1): # y=[0,1,2]
                if matrix[x][(size-1)-(y)]==matrix[x][(size-1)-(y+1)]:
                    matrix[x][(size-1)-(y)] = matrix[x][(size-1)-(y)]*2

                    for y_tmp in range(y,size-2): # y_tmp= [y,...,2]
                        matrix[x][(size-1)-(y_tmp+1)]=matrix[x][(size-1)-(y_tmp+2)]
                    matrix[x][(size-1)-(size-1)]=0

        return matrix

    if op=='up':
        for y in range(size): # x=[0,1,2,3]
            for k in range(size-1):
                for x in range(size-1): # y=[0,1,2]
                    if matrix[x][y]==0:
                        matrix[x][y]=matrix[x+1][y]
                        matrix[x+1][y]=0

                    # for x_tmp in range(x,size-2): # y_tmp= [y,...,2]
                    #     matrix[x_tmp+1][y]=matrix[x_tmp+2][y]

            for x in range(size-1): # y=[0,1,2]
                if matrix[x][y]==matrix[x+1][y]:
                    matrix[x][y] = matrix[x][y]*2

                    for x_tmp in range(x,size-2): # y_tmp= [y,...,2]
                        matrix[x_tmp+1][y]=matrix[x_tmp+2][y]
                    matrix[size-1][y]=0

        return matrix


    if op=='down':
        for y in range(size): # x=[0,1,2,3]
            for k in range(size-1):
                for x in range(size-1): # y=[0,1,2]
                    if matrix[(size-1)-(x)][y]==0:
                        matrix[(size-1)-(x)][y]=matrix[(size-1)-(x+1)][y]
                        matrix[(size-1)-(x+1)][y]=0

                    # for x_tmp in range(x,size-2): # y_tmp= [y,...,2]
                    #     matrix[(size-1)-(x_tmp+1)][y]=matrix[(size-1)-(x_tmp+2)][y]

            for x in range(size-1): # y=[0,1,2]
                if matrix[(size-1)-(x)][y]==matrix[(size-1)-(x+1)][y]:
                    matrix[(size-1)-(x)][y] = matrix[(size-1)-(x)][y]*2

                    for x_tmp in range(x,size-2): # y_tmp= [y,...,2]
                        matrix[(size-1)-(x_tmp+1)][y]=matrix[(size-1)-(x_tmp+2)][y]
                    matrix[0][y]=0

        return matrix
    



operation=product(['up','down','left','right'],repeat=5)
total=[]


for i in operation:
    matrix_copy=copy.deepcopy(matrix_original)
    
    for k in i:
    
        matrix_copy=game(matrix_copy,k)


    tot = list(chain(*matrix_copy))
    total.append(max(tot))

print(max(total))

