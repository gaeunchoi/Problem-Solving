T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))

    result = 0
    while len(prices) > 0:
        maxidx = prices.index(max(prices))
        for i in prices[:maxidx]:
            result += prices[maxidx] - i
        prices = prices[maxidx+1:]
    print(f'#{test_case} {result}')