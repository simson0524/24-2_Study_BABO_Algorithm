import sys
from itertools import combinations
N, S = map(int,sys.stdin.readline().split())
arr = list(map(int,input().split()))
cnt = 0
for i in range(1, N+1) :
    comb = combinations(arr,i)
    for c in comb : 
        if sum(c) == S : cnt+=1
print(cnt)