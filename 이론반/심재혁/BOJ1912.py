import sys
read = sys.stdin.readline

N = int(read())
arr = [0] + list(map(int, read().split()))
cache = [-1001] * (N+1)

for n in range(1, N+1):
    cache[n] = max(arr[n], cache[n-1] + arr[n])
print(max(cache))
