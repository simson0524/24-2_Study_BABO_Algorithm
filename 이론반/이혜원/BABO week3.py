# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 11:15:13 2024

@author: user
"""

#1260
#dfs 만들기
def dfs(start):  
    #start가 아직 방문 안 됐으면 방문 처리하기
    visited[start] = True
    print(start, end= ' ')
    #현재 노드와 연결된 다른 노드 재귀적 방문
    for i in graph[start]:
        if not visited[i]:
            dfs(i)  #정의된 dfs 함수 호출
            
#bfs 만들기
#초기 설정
from collections import deque  #큐를 사용하기 위해 덱 라이브러리 불러오기
n,m,v = map(int, input().split())  #정점, 간선의 개수, 시작 번호
graph = [[]*(n+1) for _ in range(n+1)]  #초기 그래프 만들기

#인접리스트 만들기
for _ in range(m):
    a,b = map(int,input().split()) 
    graph[a].append(b)   #노드 a에 연결된 노드 b의 정보 저장
    graph[b].append(a)   #노드 b에 연결된 노드 a의 정보 저장
    graph[a].sort()
    graph[b].sort()
def bfs(start):
    queue = deque([start])  #시작번호 start 에 대한 큐 정의
    #방문 안 됐으면 방문 처리하기
    visited[start] = True
      
    #큐가 빌 때까지 재귀 반복
    while queue:
        #큐에서 하나의 원소 v를 뽑아서 출력
        v = queue.popleft()
        print(v, end = ' ')
        #v와 연결된, 아직 방문되지 않은 원소들 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
        
visited = [False]*(n+1)  
dfs(v)
print()
visited = [False]*(n+1)  
bfs(v)


#11724
import sys
sys.setrecursionlimit(10**6)   #재귀제한 허용범위 넓혀주기
input = sys.stdin.readline
#초기설정 - n: 정점의 개수, m: 간선의 개수
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
#인접리스트 만들기
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)  #노드 a에 연결된 노드 b의 정보 저장
    graph[b].append(a)   #노드 b에 연결된 노드 a의 정보 저장
    
#dfs 함수 정의
def dfs(graph, v, visited):  #v: 첫번째 노드
#v 방문처리하기
    visited[v] = True
    #현재 노드와 연결된 노드를 재귀적으로 모두 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)  

#dfs 실시
cnt = 0  #cnt: 현재까지 연결된 노드의 개수
visited = [False]*(n+1)  #방문된 정보 표현하는 리스트
#dfs가 한 차례 새로 수행될 때마다 count + 1씩 함
for i in range(1,n+1):
    if not visited[i]:
        dfs(graph, i, visited)  #i번 노드가 방문되지 않았으면 새로운 dfs 수행
        cnt += 1 
print(cnt)

    
#1743
#bfs 이용
from collections import deque
import sys
input = sys.stdin.readline

#초기 설정 - n: 세로 길이, m: 가로 길이, k: 음식물 개수
n,m,k = map(int, input().split())
graph = [[0]*m for _ in range(n)]
for _ in range(k):
    r,c = map(int, input().split())
    graph[r-1][c-1] = 1  #좌표(0,0)으로 맞추기
    
#이동할 네 방향 정의(상하좌우)
dx = [1,-1,0,0]
dy = [0,0,1,-1]

#bfs 정의
def bfs(x,y):
    queue = deque([(x,y)])  #큐 초기화
    #초기 설정, cnt: 현재까지 방문한 음식물 개수
    graph[x][y] = 0  
    cnt = 1  
    
    #큐가 빌 때까지 재귀반복
    while queue:
        x,y = queue.popleft()
    #현재 위치에서 네 방향의 위치 확인 -> 음식물의 개수 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #주어진 공간 내에서 노드(음식물) 처음 방문 -> 연결된 모든 음식물(노드) 탐색
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny] = 0  #방문 처리
                cnt += 1  #count에 1 더하기
    return cnt
    
#최대 음식물 크기 탐색
result = 0
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:  #음식물이 있으면(방문되면)
        #bfs(x,y)는 현재 위치에서 탐색된 연결된 음식물의 크기, result: 탐색된 음식물의 크기 중 가장 큰 음식물 
        #새로운 음식물 크기와 기존의 가장 큰 음식물의 크기 비교하여 더 큰 값으로 갱신
            result = max(result, bfs(x,y))    
print(result)
            
                    
        

        