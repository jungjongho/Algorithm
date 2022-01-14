import math
import copy

N=int(input())
A=list(map(int,input().split()))
B,C=map(int,input().split())

pop=0
for i in range(N):
    tmp=copy.copy(A[i])
    tmp=tmp-B
    pop=pop+1
    if tmp<=0:
        pass
    else:
        pop=pop + math.ceil(tmp/C)
print(pop)