N,L=map(int,input().split())

matrix=[]

for i in range(N):
    tmp=list(map(int,input().split()))
    matrix.append(tmp)
    

def check(line):
    visit=[False]*len(line)
    for i in range(len(line)-1):
        if line[i]!=line[i+1]:
            if abs(line[i]-line[i+1])!=1:
                return 0

            elif line[i]-line[i+1]==1:
                for j in range(1,L+1):
                    try:
                        if visit[i+j]==False:
                            if line[i]-line[i+j]==1:
                                visit[i+j]=True
                                pass
                            else:
                                return 0
                        else:
                            return 0
                    except:
                        return 0


            elif line[i]-line[i+1]==-1:
                for j in range(0,L):
                    try:
                        if visit[i-j]==False:
                            if line[i-j]-line[i+1]==-1:
                                visit[i-j]=True
                                pass
                            else:
                                return 0
                        else:
                            return 0     
                    except:
                        return 0

    return 1   

time=0
for i in matrix:
    ch=check(i)
    time=time+ch

# print(time)

for i in range(len(matrix)):
    line=[]
    for j in range(len(matrix)):
        line.append(matrix[j][i])
    # print(line)

    ch=check(line)
    time=time+ch
    # print(time)

print(time)