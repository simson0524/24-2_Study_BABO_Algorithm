import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    days = int(input())
    stock_prices = list(map(int, input().split()))
    stock_prices_with_idx = []

    for idx in range(days):
        stock_prices_with_idx.append( (stock_prices[idx], idx) )

    stock_prices_with_idx.sort(reverse=True)

    curr_start_idx = 0
    earned = 0

    for price, idx in stock_prices_with_idx:
        if idx >= curr_start_idx:
            for i in range(curr_start_idx, idx):
                earned += (price - stock_prices[i])
            curr_start_idx = idx + 1

    print(earned)
