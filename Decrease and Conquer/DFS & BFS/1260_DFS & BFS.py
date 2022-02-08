n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()


visited1=[False]*(n+1)
visited2=[False]*(n+1)

def DFS(graph,v,visited):
    visited[v]=True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            DFS(graph,i,visited)


def BFS(graph,v,visited):
    queue=list([v])
    #tmp_array=[1,6]
    visited[v]=True

    while queue:
        v=queue[0]
        queue.remove(v)
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                # if queue==None:
                    # queue=[]
                queue.append(i)
                visited[i]=True

    
DFS(graph,v,visited1)
print('')
BFS(graph,v,visited2)
        