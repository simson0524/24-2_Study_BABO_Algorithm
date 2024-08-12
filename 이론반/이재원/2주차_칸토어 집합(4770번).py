import sys

def cantor_set(n):
    if n == 1:
        return "-"
    else:
        left = cantor_set(n // 3)
        empty = ' ' * (n // 3)
        right = cantor_set(n // 3)
        return left + empty + right

# 입력 방식 모르겠음 -> 입력 개수를 먼저 인풋으로 받지 않는 이상 무한루프를 사용해야해서 EOF 에러 예외처리로 동작
while True:
    try:
        num = int(sys.stdin.readline())

        answer = cantor_set(3 ** num)
        print(answer)
    except:
        break

