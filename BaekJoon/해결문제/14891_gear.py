import copy


gear=[]
for i in range(4):
    number=input()
    ok=[]
    for i in range(len(number)):
        y=number[i]
        ok.append(int(y))

    gear.append(ok)

K=int(input())

op=[]
for i in range(K):
    pp=list(map(int,input().split()))
    op.append(pp)


# print(gear)
# print(op)

def move(num,gear_list,rotation):
    
    if rotation==1:
        tmp=gear_list[num-1][0]
        gear_list[num-1][0]=gear_list[num-1][7]
        gear_list[num-1][7]=gear_list[num-1][6]
        gear_list[num-1][6]=gear_list[num-1][5]
        gear_list[num-1][5]=gear_list[num-1][4]
        gear_list[num-1][4]=gear_list[num-1][3]
        gear_list[num-1][3]=gear_list[num-1][2]
        gear_list[num-1][2]=gear_list[num-1][1]
        gear_list[num-1][1]=tmp
        return gear_list

    elif rotation==-1:
        tmp=gear_list[num-1][0]
        gear_list[num-1][0]=gear_list[num-1][1]
        gear_list[num-1][1]=gear_list[num-1][2]
        gear_list[num-1][2]=gear_list[num-1][3]
        gear_list[num-1][3]=gear_list[num-1][4]
        gear_list[num-1][4]=gear_list[num-1][5]
        gear_list[num-1][5]=gear_list[num-1][6]
        gear_list[num-1][6]=gear_list[num-1][7]
        gear_list[num-1][7]=tmp
        return gear_list






for i in op:
    gear_copy=copy.deepcopy(gear)
    if i[0]==1:
        gear_copy=move(i[0],gear_copy,i[1])
        if gear[i[0]-1][2]!=gear[i[0]][-2]:
            gear_copy=move(i[0]+1,gear_copy,-i[1])
            if gear[i[0]][2]!=gear[i[0]+1][-2]:
                gear_copy=move(i[0]+2,gear_copy,i[1])
                if gear[i[0]+1][2]!=gear[i[0]+2][-2]:
                    gear_copy=move(i[0]+3,gear_copy,-i[1])
    if i[0]==4:
        gear_copy=move(i[0],gear_copy,i[1])
        if gear[i[0]-1][-2]!=gear[i[0]-2][2]:
            gear_copy=move(i[0]-1,gear_copy,-i[1])
            if gear[i[0]-2][-2]!=gear[i[0]-3][2]:
                gear_copy=move(i[0]-2,gear_copy,i[1])
                if gear[i[0]-3][-2]!=gear[i[0]-4][2]:
                    gear_copy=move(i[0]-3,gear_copy,-i[1])

    if i[0]==2:
        gear_copy=move(i[0],gear_copy,i[1])
        if gear[i[0]-1][-2]!=gear[i[0]-2][2]:
            gear_copy=move(i[0]-1,gear_copy,-i[1])
        if gear[i[0]-1][2]!=gear[i[0]][-2]:
            gear_copy=move(i[0]+1,gear_copy,-i[1])
            if gear[i[0]][2]!=gear[i[0]+1][-2]:
                gear_copy=move(i[0]+2,gear_copy,i[1])

    if i[0]==3:
        gear_copy=move(i[0],gear_copy,i[1])
        if gear[i[0]-1][-2]!=gear[i[0]-2][2]:
            gear_copy=move(i[0]-1,gear_copy,-i[1])
            if gear[i[0]-2][-2]!=gear[i[0]-3][2]:
                gear_copy=move(i[0]-2,gear_copy,i[1])
        if gear[i[0]-1][2]!=gear[i[0]][-2]:
            gear_copy=move(i[0]+1,gear_copy,-i[1])


    gear=gear_copy    

    for i in gear_copy:
        print(i)
    for i in gear:
        print(i)


    print('==='*20)




for i in gear_copy:
    print(i)

point=0

for idx,i in enumerate(gear_copy):
    if i[0]==1:
        point = point + 2**(idx)

print(point)


