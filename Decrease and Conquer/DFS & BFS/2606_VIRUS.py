n=int(input())
m=int(input())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited1=[False]*(n+1)
visited2=[False]*(n+1)

check=[]

def DFS(graph,v,visited):
    visited[v]=True
    check.append(v)

    for i in graph[v]:
        if not visited[i]:
            DFS(graph,i,visited)

DFS(graph,1,visited1)

print(len(check)-1)
