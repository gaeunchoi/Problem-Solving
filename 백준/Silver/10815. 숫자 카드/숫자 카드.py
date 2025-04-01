N = int(input())
sanggeun = set(map(int, input().split()))

M = int(input())
nums_list = list(map(int, input().split()))

answer = [-1 for _ in range(M)]
for i in range(M):
    answer[i] = 1 if nums_list[i] in sanggeun else 0

print(*answer)
