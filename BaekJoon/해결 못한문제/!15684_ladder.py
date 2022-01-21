from itertools import combinations
import copy

N,M,H=map(int,input().split())

check_list=[]
for i in range(M):
    tmp=list(map(int,input().split()))
    check_list.append(tmp)

ladder = [[0]*N for _ in range(H)]
ladder.append(list(range(0,N)))

for i in check_list:
    ladder[i[0]-1][i[1]-1]=106
    ladder[i[0]-1][i[1]]=104

def down(ladder,number):
    
    for i in range(len(ladder)):
        if ladder[i][number]==104:
            number=number-1
        elif ladder[i][number]==106:
            number=number+1

    return ladder[len(ladder)-1][number]

def add(ladder,location):
    
    ladder_copy=copy.deepcopy(ladder)

    if ladder_copy[location[0]][location[1]]==0:
        ladder_copy[location[0]][location[1]]=106
        ladder_copy[location[0]][location[1]+1]=104     

        return ladder_copy

    else:
        return -1

def check(ladder):
    t=0
    for i in range(N):
        if down(ladder,i)==i:
            t=t+1
            # print(t)   
    if t == len(ladder[0]):
        return 1
    else:
        return -1

space=[]
for i in range(len(ladder)-1):
    tmp=[]
    for j in range(len(ladder[0])):
        if ladder[i][j]==0:
            tmp.append(j)
    space.append(tmp)


space_index=[]
for idx, i in enumerate(space):
    tmp=[]
    for j in range(len(i)-1):
        if i[j]+1==i[j+1]:
            tmp.append((idx,i[j]))
    space_index.extend(tmp)

space_index2=list(combinations(space_index,2))
space_index3=list(combinations(space_index,3))


q=0

a=check(ladder)
if a==1:
    print(0)
    q=42

if q!=42:
    for i in space_index:
        check_ladder=add(ladder,i)
        a=check(check_ladder)
        if a==1:
            print(1)
            q=42
            break

if q!=42:
    for i in space_index2:
        check_ladder=add(ladder,i[0])
        check_ladder2=add(check_ladder,i[1])
        if (check_ladder==-1) or (check_ladder2==-1):
            pass
            
        else:
            a=check(check_ladder2)
        if a==1:
            print(2)
            q=42
            break

if q!=42:
    for i in space_index3:
        check_ladder=add(ladder,i[0])
        check_ladder2=add(check_ladder,i[1])
        if check_ladder2!=-1:
            check_ladder3=add(check_ladder2,i[2])

        if (check_ladder==-1) or (check_ladder2==-1) or (check_ladder3==-1):
            continue
        else:
            a=check(check_ladder3)
        if a==1:
            print(3)
            q=42
            break

if q!=42:
    print(-1)