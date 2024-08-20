from collections import deque

# BFS
def bfs(x, y):
  res = 0  # 음식물 크기
  queue = deque()
  # 시작 지점 삽입, 방문 표시
  queue.append((x, y))
  graph[x][y] = 0

  while queue:
    x, y = queue.popleft()
    res += 1  # 음식물 추가
    # 상하좌우 탐색
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 범위 내이고 음식물이면
      if(0 <= nx < n and 0 <= ny < m):
        if(graph[nx][ny] == 1):
          # 삽입, 방문 표시
          queue.append((nx, ny))
          graph[nx][ny] = 0
  return res       

# 세로, 가로, 음식물 총 개수
n, m, k = map(int, input().split())
size = []  # 음식물 크기
graph = [[0] * m for _ in range(n)]  # n*m
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 음식물 좌표 입력받기
for _ in range(k):
  r, c = map(int, input().split())
  graph[r - 1][c - 1] = 1  # 음식물 표시


for i in range(n):
  for j in range(m):
    # 음식물이 있는 좌표에서 bfs()호출
    if(graph[i][j] == 1):
      size.append(bfs(i, j))

print(max(size))