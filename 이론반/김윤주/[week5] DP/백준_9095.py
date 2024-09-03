"""
dp[1]	1	                                                          1
dp[2]	1+1, 2	                                                      2
dp[3]	1+1+1, 1+2, 2+1, 3                                            4
dp[4]	1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1                   7
dp[5]	1+1+1+1+1, 1+1+1+2 (4개), 1+1+3 (3개), 1+2+2 (3개), 2+3 (2개)   13
...
점화식 -> dp[x] = df[x-1] + df[x-2] + df[x-3]
"""

import sys
input = sys.stdin.readline

T = int(input())

dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(0,T):
    ans = int(input())
    print(dp[ans])