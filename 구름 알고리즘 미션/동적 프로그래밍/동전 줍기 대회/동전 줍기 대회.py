import sys
input = sys.stdin.readline

N = int(input())
coins = list(map(int, input().split()))

pickCoins = [0] * N
pickCoins[0] = coins[0]
for i in range(1, N):
		pickCoins[i] = max(coins[i], coins[i] + pickCoins[i-1])

print(max(pickCoins) if max(pickCoins) > 0 else 0)