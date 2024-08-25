import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n) : 
    start,end = map(int,sys.stdin.readline().split())
    arr.append((start,end))
arr.sort(key=lambda x : (x[1],x[0]))
count = 1
end = arr[0][1]
for i in range(1,n) : 
    if arr[i][0]>=end :
        end = arr[i][1]
        count+=1
print(count)