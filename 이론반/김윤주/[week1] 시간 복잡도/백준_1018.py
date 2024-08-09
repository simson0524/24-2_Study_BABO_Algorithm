from sys import stdin

n, m = map(int, stdin.readline().split())

# 정상 체스판
board_1 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ]

board_2 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
           ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
           ]


board = []
for i in range(n):
    board.append(list(map(str, input().rstrip())))


results = []
# board에서 8x8 크기의 모든 부분 영역 확인
for i in range(n - 7):
    for j in range(m - 7):
        result_1 = 0
        result_2 = 0
        temp = [row[j:8+j] for row in board[i:8+i]]
        
        # temp의 각 요소를 board_1과 board_2의 대응되는 요소와 비교
        for k in range(8):
            for h in range(8):
              if temp[k][h] == board_1[k][h]:
                  result_1 += 1
              if temp[k][h] == board_2[k][h]:
                  result_2 += 1

        results.append(min(result_1, result_2))

print(min(results))