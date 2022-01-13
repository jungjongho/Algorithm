from itertools import chain
from itertools import combinations
import copy





N,M=map(int,input().split())
matrix_original=[]
for i in range(N):
    number=list(map(int,input().split()))
    matrix_original.append(number)

matirx_flatten=list(chain(*matrix_original))


#flatten에서 공간의 위치와 virus의 위치뽑기
air_index=[]
virus_index=[]
for idx,i in enumerate(matirx_flatten):
    if i==0:
        air_index.append(idx)
    elif i==2:
        virus_index.append(idx)


# virus를 전염시키는 함수

def infection(matrix,location):
    if matrix[location]==2:
        if location==0:
            if matrix[location+1]==0:
                matrix[location+1]=2
                infection(matrix,location+1)
            if matrix[location+M]==0:
                matrix[location+M]=2
                infection(matrix,location+M)

        elif location==M-1:
            if matrix[location-1]==0:
                matrix[location-1]=2
                infection(matrix,location-1)
            if matrix[location+M]==0:
                matrix[location+M]=2
                infection(matrix,location+M)

        elif location==(N*M-1):
            if matrix[location-1]==0:
                matrix[location-1]=2
                infection(matrix,location-1)
            if matrix[location-M]==0:
                matrix[location-M]=2
                infection(matrix,location-M)

        elif location==(N-1)*(M):
            if matrix[location+1]==0:
                matrix[location+1]=2
                infection(matrix,location+1)
            if matrix[location-M]==0:
                matrix[location-M]=2
                infection(matrix,location-M)

        elif 0<location<M-1:
            if matrix[location-1]==0:
                matrix[location-1]=2
                infection(matrix,location-1)
            if matrix[location+1]==0:
                matrix[location+1]=2
                infection(matrix,location+1)
            if matrix[location+M]==0:
                matrix[location+M]=2
                infection(matrix,location+M)

        elif (N-1)*M<location<N*M-1:
            if matrix[location-1]==0:
                matrix[location-1]=2
                infection(matrix,location-1)
            if matrix[location+1]==0:
                matrix[location+1]=2
                infection(matrix,location+1)
            if matrix[location-M]==0:
                matrix[location-M]=2
                infection(matrix,location-M)

        elif location % M ==0:
            if matrix[location+1]==0:
                matrix[location+1]=2
                infection(matrix,location+1)
            if matrix[location+M]==0:
                matrix[location+M]=2
                infection(matrix,location+M)
            if matrix[location-M]==0:
                matrix[location-M]=2
                infection(matrix,location-M)

        elif location % M == M-1:
            if matrix[location-1]==0:
                matrix[location-1]=2
                infection(matrix,location-1)
            if matrix[location-M]==0:
                matrix[location-M]=2
                infection(matrix,location-M)
            if matrix[location+M]==0:
                matrix[location+M]=2
                infection(matrix,location+M)

        else:
            if matrix[location+1]==0:
                matrix[location+1]=2
                infection(matrix,location+1)
            if matrix[location-1]==0:
                matrix[location-1]=2
                infection(matrix,location-1)
            if matrix[location+M]==0:
                matrix[location+M]=2
                infection(matrix,location+M)
            if matrix[location-M]==0:
                matrix[location-M]=2
                infection(matrix,location-M)



# 벽을 놓을 3개의 location 찾기

air_combination=list((combinations(air_index,3)))


count=[]

for i in air_combination:
    matrix_flatten_copy=copy.deepcopy(matirx_flatten)

    for k in i:
        matrix_flatten_copy[k]=1

    for j in virus_index:
        infection(matrix_flatten_copy,j)

    count.append(matrix_flatten_copy.count(0))

print(max(count))
