#백준 1018
n,m = map(int,input().split())
board = []

for _ in range(n):
    board.append(input())

res = float('inf')

for i in range(n-7):
    for j in range(m-7):
        white = 0
        black = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                pos = k+l
                if (pos%2==0):
                    if(board[k][l] != 'B'):
                        black += 1
                    if(board[k][l] != 'W'):
                        white += 1
                else:
                    if(board[k][l] != 'W'):
                        black += 1
                    if(board[k][l] != 'B'):
                        white += 1         
        res = min(res,white,black)

print(res)



#백준 11870
n = int(input())
arr = list(map(int,input().split()))
sort_list = sorted(set(arr))
dic = {}

for i in range(len(sort_list)):
    dic[sort_list[i]] = i

for i in arr:
    print(dic[i],end=" ")




########
#프로그래머스 연속된 부분 수열의 합
def solution(sequence,k):
    rp = 0 
    lp = 0
    temp = sequence[lp]
    answer = []
    li = list()

    while lp <= rp < len(sequence):
        if temp == k:
            answer.append([lp,rp])        
            temp -= sequence[lp]
            lp +=1

        elif temp < k:
            rp +=1
            if(rp<len(sequence)):
                temp += sequence[rp]
        else:
            temp -= sequence[lp]
            lp +=1

    answer = min(answer,key = lambda x: (x[1]-x[0],x[0]))
    return answer