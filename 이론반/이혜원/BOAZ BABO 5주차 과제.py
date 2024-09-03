# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 11:09:30 2024

@author: user
"""

#11726
#n에 대하여 피보나치 수열로 직사각형을 채우는 방법의 수가 늘어남..1,2,3,5,8 => 바텀업방법 사용
#초기설정
n = int(input())
d = [0]*(n+1)
d[1] = 1
if n>1:
    d[2] = 2

for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n] % 10007)


#9095
#d[1]= 1, d[2] = 2, d[3] = 4, d[4] = 7, d[5] = 13 => d[n>=4]부터 n이전의 3개 항의 합이 d[n]의 값이 되는 피보나치 수열
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    n = int(input())
    d = [0]*(n+1)
    
    for i in range(1,n+1):
        if i == 1:
            d[i] = 1
        elif i == 2:
            d[i] = 2
        elif i == 3:
            d[i] = 4
        else:
            d[i] = d[i-1] + d[i-2] + d[i-3]
    print(d[n])