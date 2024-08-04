import sys
chess=[['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
n,m = map(int,sys.stdin.readline().split())
total =n*m
board = []
for _ in range(n) :
    board.append(list(sys.stdin.readline().strip('\n')))
def check(a,b) :
    cnt = 0
    for i in range(8) :
        for j in range(8) : 
            if chess[i][j] == board[a+i][b+j] : cnt+=1
    return min(cnt, 64-cnt)
for i in range(n-7) :
    for j in range(m-7) :
        total = min(total,check(i,j))
print(total)



