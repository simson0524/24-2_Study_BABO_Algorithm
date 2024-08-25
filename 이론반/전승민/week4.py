#1931
N = int(input())
cnt = 0
arr = []
for _ in range(N):
    a,b = map(int,input().split())
    arr.append([a,b])

arr.sort(key= lambda x :(x[1],x[0]))
#(1,4) (3,5) (0,6) (5,7) (3,8) ....
temp = 0
for start, end in arr:
    if start >= temp:
        cnt+=1
        temp = end

print(cnt)

# 11501
T = int(input())

for _ in range(T):
    N = int(input())
    temp = list(map(int,input().split()))

    res = 0
    sell = 0 # 매도 가격

    for i in range(len(temp)-1,-1,-1):
        if temp[i] > sell:
            sell = temp[i]
        else:
            res += sell-temp[i]
    
    print(res)


# 1912
N = int(input())
li = list(map(int,input().split()))

temp = N*[0] # 축적 시키는거
temp[0] = li[0]
for i in range(1,N):
    temp[i] = max(li[i]+temp[i-1],li[i])
print(max(temp))

