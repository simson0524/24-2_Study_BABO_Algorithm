import sys

# 재귀 최대깊이, dfs 사용 시 오류 방지
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# 정점의 개수 n, 간선의 개수 m
n, m = map(int, input().split())

# 인접행렬 graph
graph = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 방문 내역 표시
visited = [0] * (n+1)

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)

count = 0
for root in range(1, n+1):
    if visited[root] == 0:
        count+=1
        dfs(root)

print(count)