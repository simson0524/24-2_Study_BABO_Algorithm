import sys
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
numbers_B = sorted(set(numbers))
changed = []

for i in numbers:
    count = 0
    for j in range(len(numbers_B)):
        if numbers_B[j] < i:
            count += 1
    changed.append(count)

for i in changed:
    print(i, end=' ')






