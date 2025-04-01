N, M = map(int, input().split())

first = []
second = []

for i in range(N):
    num = list(map(int, input().split()))
    first.append(num)

for i in range(N):
    num = list(map(int, input().split()))
    second.append(num)

for i in range(N):
    for j in range(M):
        print(first[i][j] + second[i][j], end = ' ')
    print()
