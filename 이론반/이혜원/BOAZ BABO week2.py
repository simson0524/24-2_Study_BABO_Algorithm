# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 19:41:03 2024

@author: user
"""
#4779
import sys
input = sys.stdin.readline
#cantor 정의 - length(구간길이)가 1이 될때 재귀 멈춤, a: 시작점, b:끝점
def cantor(length, a, b):
    if length == 1:
        return
    
    #n = 3등분한 구간의 길이
    n = (b - a) // 3
     #가운데 공백으로 두기
    for i in range(a + n, a + 2*n):
        result[i] = ' '   
    #왼쪽 재귀
    cantor(n, a, a + n)
    #오른쪽 재귀
    cantor(n, a + 2*n, b)
    
while True:
    try:
        length = int(input().strip())    
        result = ['-'] * (3**length)
        cantor(3**length, 0, 3**length)
        print(''.join(result))
    except:
        break
    
        
#1182
import sys
input = sys.stdin.readline

#초기 설정... N: 리스트 길이,  S: 부분수열 원소의 합, N_list = 원래 리스트 / cnt: 원소의 합=S인 부분수열 개수, x = cnt를 만족시키는 원소 리스트
N,S = map(int, input().split())
N_list = list(map(int, input().split()))
cnt = 0
x = []
#각 인덱스의 중복을 피하기 위한 인덱스 사용 여부 파악
visited = [False]*N
 #a: 인덱스 시작점
def dfs(a, x):
    global cnt
    if sum(x) == S and len(x) > 0:
        cnt += 1
        
    #N 탐색 => '백트랙킹' - i번째 원소가 아직 visited 안 됐다면...
    #i번째 원소 표시-> N_list의 i번째 원소 x 리스트에 추가-> 다음 인덱스 탐색-> 현재 원소 방문 취소-> 제거
    for i in range(a, N):
        if not visited[i]:
            visited[i] = True
            x.append(N_list[i])
            dfs(i + 1, x)
            visited[i] = False
            x.pop()
dfs(0,x)
print(cnt)


#1759
#L: 암호의 길이, C: 문자 종류 가짓수/ cnt:현재 암호의 길이, idx: 인덱스
def dfs(cnt, idx):
    if cnt == L:
        #자음, 모음 갯수 세기...ArithmeticErrora,e,i,o,u 안에 있으면 모음, 아니면 자음
        consonant, vowel = 0,0
        for r in result:
            if r in 'aeiou': vowel += 1
            else: consonant += 1
            
        #자음의 갯수>=2, 모음 갯수>= 1인 경우만 count
        if consonant >= 2 and vowel >= 1:
                print(''.join(result))
        return
                
    # 알파벨 배열 탐색=>'백트랙킹' - i번째 알파벳이 아직 visited 안 됐다면...
    #i번째 알파벳 표시-> 결과에 추가하여 조합 저장-> 다음 인덱스로 이동-> i번째 알파벳 방문 취소->제거
    for i in range(idx, C):
        if not visited[i]:
            visited[i] = True
            result.append(alphabet[i])
            dfs(cnt + 1, i + 1 )
            visited[i] = False
            result.pop()
                            
#초기 설정
L,C= map(int, input().split())
alphabet = input().split()
alphabet.sort()
#visited = 방문 안 된(조합에 추가가 안 된) 문자 종류 가짓수(C)
visited = [False]*C
result = []
dfs(0,0)

