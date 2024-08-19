from collections import deque

# 정점의 개수 n, 간선의 개수 m, 시작노드 v
n, m, v = map(int, input().split())

# 인접행렬 graph
graph = [[0] * (n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited1 = [0] * (n+1)
visited2 = [0] * (n+1)

# DFS
def dfs(v):
    visited1[v] = 1
    print(v, end=' ')

    for i in range(1, n+1):
        if visited1[i] == 0 and graph[v][i] == 1:
            dfs(i)

# BFS
def bfs(v):
    # 방문해야할 곳을 순서대로 넣을 큐
    queue = deque([v])
    visited2[v] = 1

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visited2[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited2[i] = 1

dfs(v)
print()
bfs(v)