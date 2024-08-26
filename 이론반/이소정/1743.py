import sys
from collections import deque
n,m,k = map(int, sys.stdin.readline().split())

# 비재귀로 풀어보기

def dfs(graph,start_node) :
    to_visit, visited = deque(), []
    to_visit.append(start_node)
    while 
    