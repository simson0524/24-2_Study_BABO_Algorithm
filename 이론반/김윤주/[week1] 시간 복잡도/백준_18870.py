import sys

# 찾으면 index를, 찾지 못하면 -1을 반환
def binary_search(lis, target):
    low, high = 0, len(lis) - 1

    while low <= high:
        mid = (low + high) // 2
        if lis[mid] < target:
            low = mid + 1
        elif lis[mid] > target:
            high = mid - 1
        else:
            return mid  
    return -1  


_ = int(sys.stdin.readline().strip())
li = list(map(int,sys.stdin.readline().split()))

# 증복 제거 후 정렬
data_set = sorted(set(li))


results = []
dic = {}

# 각 요소가 이미 dic에 있는지 확인 -> 없다면 이진 탐색 수행하여 인덱스 찾기
for i in range(len(li)):
    if(dic.get(li[i])==None):
        cnt = binary_search(data_set,li[i])
        dic[li[i]]=cnt
    
    # 공백 구분하여 출력
    if(i<len(li)):
        print(dic[li[i]],end=" ")
    else:
        print(dic[li[i]])