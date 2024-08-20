import sys
from collections import deque
N, M, V = map(int, sys.stdin.readline().split())
explore = [[False]*(N+1) for _ in range(N+1)]

for _ in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    explore[a][b] = 1
    explore[b][a] = 1

visited1 = [False] * (N+1)
visited2 = [False] * (N+1)

def dfs(V) : 
    visited1[V] = True
    print(V, end=" ")
    for i in range(1, N+1) :
        if not visited1[i] and explore[V][i]  == 1 :
            dfs(i)
               

def bfs(V) :
    q = deque([V])
    visited2[V] = True
    while q :
        V = q.popleft()
        print(V, end=" ")
        for i in range(1,N+1) :
            if not visited2[i] and explore[V][i] == 1 :
                q.append(i)
                visited2[i] = 1

dfs(V)
print()
bfs(V)
       