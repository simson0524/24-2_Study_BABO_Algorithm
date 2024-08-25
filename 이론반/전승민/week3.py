#1260
from collections import deque

N,M,V = map(int,input().split())
# N=4
# M=5
# V=1
graph = [[]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

#graph = [[],[2,3,4],[1,4],[1,4],[1,2,3]]
def dfs(graph,start_node):
    to_visitd = list()
    visitedd = list()
    to_visitd.append(start_node)

    while to_visitd:
        node = to_visitd.pop()

        if node not in visitedd:
            visitedd.append(node)
            to_visitd.extend(sorted(graph[node],reverse=True))
    return visitedd

def bfs(graph,start_node):
    to_visitb = deque()
    visitedb = list()
    to_visitb.append(start_node)

    while to_visitb:
        node = to_visitb.popleft()

        if node not in visitedb:
            visitedb.append(node)
            to_visitb.extend(graph[node])
    return visitedb 

print(*dfs(graph, V))
print(*bfs(graph, V))


# 11724

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

temp_visited = [False]*(N+1)

def calc(node):
    temp_visited[node] = True

    for k in graph[node]:
        if temp_visited[k] == False: 
            calc(k)
count = 0
for i in range(1, N+1):
    if temp_visited[i] == False:
        calc(i) 
        count += 1

print(count)

# 1743
import sys
sys.setrecursionlimit(10**7)

#dx,dy이용..
dx = [0,0,-1,1]
dy = [-1,1,0,0]
N,M,K = map(int,input().split())
answer = 0
graph = [[0]*M for _ in range(N)]
for _ in range(K):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1

visited = [[False]*M for _ in range(N)]

def dfs(a,b):
    global count
    count+=1
    visited[a][b] =True
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if N> nx >= 0 and M> ny >=0 and graph[nx][ny] ==1 and visited[nx][ny] == False:
            dfs(nx,ny)

for i in range(N):
    for j in range(M):
        if visited[i][j] == False and graph[i][j]==1:
            count = 0
            dfs(i,j)
            answer = max(answer,count)


print(answer)
