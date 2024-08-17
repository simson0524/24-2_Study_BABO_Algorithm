#백준 1018 -----나중에 다시보기
##########

n,m = map(int,input().split())
#n= 8
#m=8
board = []
#board = [
#['W','B','W','B','W','B','W','B'],
#['B','W','B','W','B','W','B','W'],
#['W','B','W','B','W','B','W','B'],
#['B','W','B','W','B','W','B','W'],
#['W','B','W','B','W','B','W','B'],
#['B','W','B','W','B','W','B','W'],
#['W','B','W','B','W','B','W','B'],
#['B','B','B','W','B','W','B','W']
#]

for _ in range(n):
    board.append(input())

res = float('inf')

# 8x8 맞춰야함 
for i in range(n-7):
    for j in range(m-7):
        #8x8 시작점 색 
        white = 0 #시작점이 흰색일때 바뀌는 개수
        black = 0 #시작점이 검정일때 바뀌는 개수
        for k in range(i, i+8):
            for l in range(j, j+8):
                pos = k+l
                #좌표합이 짝수, 짝수 끼리는 같아야함
                if (pos%2==0):
                    if(board[k][l] != 'B'):
                        black += 1 #첫번째가 검정일때, 현재칸 검정으로 바꿈
                    if(board[k][l] != 'W'):
                        white += 1 #첫번째가 흰색일때, 현재칸 흰색으로 바꿈
                else:
                    if(board[k][l] != 'W'):
                        black += 1 #첫번째가 검정일때, 현재칸 흰색으로 바꿈
                    if(board[k][l] != 'B'):
                        white += 1 #첫번째가 흰색일때, 현재칸 검정으로 바꿈   
                #print('(k,l)',k,l,' white: ', white,' , black: ',black)            
        res = min(res,white,black)
        #print('res: ',res)

print(res)
                    

#######
#백준 11870
n = int(input())
arr = list(map(int,input().split()))

#정렬,중복제거..
sort_list = sorted(set(arr))

#딕셔너리로 묶어버리면됨..
dic = {}

for i in range(len(sort_list)):
    dic[sort_list[i]] = i

for i in arr:
    print(dic[i],end=" ")




########
#프로그래머스 연속된 부분 수열의 합
#포인터 이용해서 비교...
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
