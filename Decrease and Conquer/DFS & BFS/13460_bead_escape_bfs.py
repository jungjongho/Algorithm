from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]
# check_red=[[False]*m]*n
# check_blue=[[False]*m]*n
# check=[[[[[False]*m]*n]*m]*n]

# check_red=[[False]*m for _ in range(n)]

# check_blue=[[False]*m for _ in range(n)]
# 
check = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]



#왜 굳이 check에서 R 과 B를 한곳에 넣어주었을까?
#R,B를 함께해서 10^4번보다는 R과B를 따로따로 10^2, 10^2에 넣어주는 편이 보기에 편하지 않았을까?


dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
q = deque()


def init(): #시작 R지점과 B지점 확보
    rx, ry, bx, by = [0]*4

    for i in range(n):
        for j in range(m):
            if a[i][j] == 'R':
                rx, ry = i, j
            elif a[i][j] == 'B':
                bx, by = i, j
    q.append((rx, ry, bx, by, 0))
    print(q)
    # check_red[rx][ry] = True
    # check_blue[bx][by] = True
    # check[rx][ry][bx][by]=True


def move(x, y, dx, dy, c):
    while a[x+dx][y+dy] != '#' and a[x][y] != 'O': # #에막힐 떄까지 c가 한방향으로 이동
        x += dx
        y += dy
        c += 1
    return x, y, c

def bfs():
    while q:
        rx1, ry1, bx1, by1, d = q.popleft() #q에 담겨있는 r,b의 위치를 가져옴 q는 비어있음
        print('pop: ',q)
        # print(q)
        if d >= 10:
            break
        for i in range(4): #0,1,2,3  0->left, 1-> down, 2->right, 3-> up
            nrx, nry, rc = move(rx1, ry1, dx[i], dy[i], 0) # dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
            nbx, nby, bc = move(bx1, by1, dx[i], dy[i], 0)
            if a[nbx][nby] == 'O': #파란공이 O에 들어갔을 때
                continue
            if a[nrx][nry] == 'O': #빨간공이 O에 들어갔을 때
                print(d+1)
                return
            if nrx == nbx and nry == nby: #빨간공과 파란공이 겹쳤을 때
                if rc > bc: #더 많이 움직인것이 R인 경우
                    nrx, nry = nrx-dx[i], nry-dy[i]   # R공을 한칸 뒤로 
                else:# 더 많이 움직인것이 B인경우
                    nbx, nby = nbx-dx[i], nby-dy[i] # B공을 한칸 뒤로
            # if ((check_red[nrx][nry]==False) and (check_blue[nbx][nby]==False)): #그 파트에 들어온적이 없다면 
                # check_red[nrx][nry] ,check_blue[nbx][nby] = True, True #방문 표시한뒤에
            if check[nrx][nry][nbx][nby]==False:
                check[nrx][nry][nbx][nby]=True
                q.append((nrx, nry, nbx, nby, d+1)) # q에 추가
                print('i:',i)
                print('q:',q)
        print('finsh :',q)

    print(-1)

init()
bfs()



