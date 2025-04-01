import sys

N = int(sys.stdin.readline())

roads = list(map(int, sys.stdin.readline().rstrip().split()))
prices = list(map(int, sys.stdin.readline().rstrip().split()))

result = 0
money = prices[0]

for i in range(N-1):
    if prices[i] < money:
        money = prices[i]

    result += money * roads[i]

print(result)
