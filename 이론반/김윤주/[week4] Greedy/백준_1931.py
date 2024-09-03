import sys
n = int(sys.stdin.readline())

timeline = []
for i in range(n):
    start, end = map(int,sys.stdin.readline().split())
    timeline.append((start, end))
# 회의가 끝나는 시간을 기준으로 정렬
timeline.sort(key=lambda x : (x[1], x[0]))

# 첫 번째 회의(index=0) 무조건 포함
count = 1
end = timeline[0][1]

for i in range(1, n):
    if timeline[i][0]>=end:
        end = timeline[i][1]
        count += 1

print(count)