# 풀이법을 생각해내지 못해서, 솔루션을 보고 이해했습니다..

def solution(sequence, k):
    answer = []
    n = len(sequence)
    s,end = 0, 0
    for i in range(len(sequence)):
        while s < k and end < n:
            s += sequence[end]
            end += 1
        if s == k:
            answer.append((i,end-1))
        s -= sequence[i]
            
    return sorted(answer,key=lambda x: x[1]-x[0])[0]