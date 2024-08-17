n, s = map(int, input().split())
arr = list(map(int, input().split()))

final_index = n-1
cnt = 0

def bfs(curr_sum, idx):
    global arr, final_index, cnt, n, s
    now = curr_sum + arr[idx]
    for i in range(idx+1, n):
        bfs(now, i)
    
    if now == s:
        cnt += 1


for i in range(n):
    bfs(0, i)

print(cnt)
