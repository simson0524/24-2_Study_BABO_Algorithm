import sys
sys.setrecursionlimit(10**6)
n,m = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(n+1)]
visited = [False]*(n+1)
cnt=0

for _ in range(m) : 
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# DFS
def dfs(v) : 
    visited[v] = True
    for i in graph[v] :
        if not visited[i] : # 방문하지 않은 노드라면
            dfs(i) # 재귀 호출

for i in range(1,n+1) :
    if not visited[i] : # 해당 정점이 방문하지 않았다면
        dfs(i)
        cnt += 1

print(cnt)
        