import sys

N, K = map(int, sys.stdin.readline().split())

money = []
for _ in range(N):
    money.append(int(sys.stdin.readline()))

cnt = 0
for i in reversed(range(N)):
    cnt += K // money[i]
    K = K % money[i]

print(cnt)