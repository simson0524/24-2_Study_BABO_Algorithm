import sys

# 재귀 최대깊이, dfs 사용 시 오류 방지
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# 가로 길이 n, 세로 길이 m, 쓰레기 개수 k
n, m, k = map(int, input().split())

# 쓰레기 위치 인접 행렬 graph
graph = [[0] * m for _ in range(n)]

for _ in range(k):
  r, c = map(int, input().split())
  graph[r - 1][c - 1] = 1

# 방문 내역 표시
visited = [[0] * m for _ in range(n)]

# 상하좌우 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y):
  global num
  num += 1
  visited[x][y] = 1

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    # 현재 (nx, ny) 좌표가 입력 범위 내에 있는지 확인
    if 0 <= nx and nx < n and 0 <= ny and ny < m:
      if graph[nx][ny] == 1 and visited[nx][ny] == 0:
        dfs(nx, ny)

result = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1 and not visited[i][j]:
      num = 0
      dfs(i, j)
      result = max(result, num)
      
print(result)