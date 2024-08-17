# 너무 어려우요...

vowel = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, input().split())
words = input().split()

words.sort() 

def check(arr):
    v_count, c_count = 0, 0 # 모음 개수, 자음 개수

    for i in arr:
        if i in vowel:
            v_count += 1
        else:
            c_count += 1

    if v_count >= 1 and c_count >= 2:
        return True
    else:
        return False

def backtracking(arr):
    # 길이가 맞으면 자음 모음 체크하고 내보내기
    if len(arr) == L:
        if check(arr):
            print("".join(arr))
            return
    # 길이 안맞으면 순서 고려해서 알파벳 추가
    for i in range(len(arr), C):
        if arr[-1] < words[i]:
            arr.append(words[i])
            backtracking(arr)
            arr.pop()

for i in range(C - L + 1):
    a = [words[i]]
    backtracking(a)