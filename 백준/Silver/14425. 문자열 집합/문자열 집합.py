answer = 0

N, M = map(int, input().split())

strs = set()
for _ in range(N):
    strs.add(input())

for _ in range(M):
    if input() in strs:
        answer += 1

print(answer)