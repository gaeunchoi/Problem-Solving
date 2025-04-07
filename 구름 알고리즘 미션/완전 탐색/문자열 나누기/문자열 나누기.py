N = int(input())
S = input()

result = []
for i in range(1, N - 1):
    for j in range(i + 1, N):
        part1 = S[:i]
        part2 = S[i:j]
        part3 = S[j:]
        result.append([part1, part2, part3])

# 모든 부분문자열 수집 후 중복 제거하고 정렬
flat = []
for r in result:
    flat.extend(r)
P = sorted(set(flat))

# 점수 계산
max_score = 0
for part1, part2, part3 in result:
    i = P.index(part1)
    j = P.index(part2)
    k = P.index(part3)
    score = i + j + k + 3
    max_score = max(max_score, score)

print(max_score)
