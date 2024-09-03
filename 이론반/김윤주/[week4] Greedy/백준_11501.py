import sys

def get_max_profit(N, price):
    result = 0

    # j -> 최대값 index
    j = N - 1
    
    for i in range(N - 2, -1, -1):
        if price[i] < price[j]:
            result += price[j] - price[i]
        else:
            j = i
    
    return result

T = int(sys.stdin.readline())
results = []
    
for _ in range(T):
    N = int(sys.stdin.readline())
    price = list(map(int, input().split()))
    results.append(get_max_profit(N, price))
    
for result in results:
    print(result)