# n=2 -> 2개
# n=3 -> 3개
# n=5 -> 8개
# 앞의 두 개의 합이 현재 -> 피보나치?

n = int(input())
memo = [0 for _ in range(1000)] #조건에 따라 1000으로 설정

def tiling(n):
    if n == 1:
        return 1  #0이라 영향 안미침
    
    if n == 2:
        return 2

    if memo[n] != 0:
        return memo[n]
    
    memo[n] = (tiling(n-2) + tiling(n-1)) % 10007
    return memo[n]

print(tiling(n))

