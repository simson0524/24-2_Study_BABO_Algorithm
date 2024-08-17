# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 23:11:41 2024

@author: user
"""
#Q1) 다시 칠해야하는 체스보드 칸의 수 계산
def repaint(board, start_row, start_col, first_color):
    repaint_count = 0
    current_color = first_color
    
    for i in range(8):
        for j in range(8):
            if board[start_row + i][start_col + j] != current_color:
                repaint_count += 1
            current_color = 'B' if current_color == 'W' else 'W'
        current_color = 'B' if current_color == 'W'else 'W'
    return repaint_count

#88 보드를 선택하여 최소로 칠해야하는 칸의 수 찾기
def min_repaint(board,N,M):
    min_repaint_needed = float('inf') 
    
    for i in range(N-7):
        #흰색으로 시작/ 검은색으로 시작할때 검사
        for j in range(M-7):
            white_start = repaint(board, i, j, 'W')
            black_start = repaint(board, i, j, 'B')
            #둘 중 더 작은 값 선택하여 min_reapaint_needed에 새로 갱신
            min_repaint_needed = min(min_repaint_needed, white_start, black_start)
            
    return min_repaint_needed

#입력 받기
N,M = map(int, input().split())
board = [input().strip() for _ in range(N)]

print(min_repaint(board,N, M))



#Q3) 투포인터 기법
# 변수 초기화
def solution(sequence, k):
    n = len(sequence)
    l, r = 0, 0
    cur_sum = 0
    start, end = 0, n
    min_len = n+1
    #right 포인터가 마지막 인덱스에 도달할 때까지 반복
    while r < n:
        cur_sum += sequence[r]
        #현재 수열이 k보다 클동안 반복
        while cur_sum >= k:
            #합이 k일때- 수열 길이 계산
            if cur_sum == k:
                current_len = r - l + 1
                #현재 수열 길이가 최소길이보다 작거나 인덱스가 작을 때 갱신
                if current_len < min_len or (current_len == min_len and l < start):
                    start, end = l, r
                    min_len = current_len
                #현재 부분수열 합에서 왼쪽 포인터 값 제외
            cur_sum -= sequence[l]
            l += 1
            
        r += 1
    return [start, end] 