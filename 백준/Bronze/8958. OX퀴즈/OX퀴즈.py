n = int(input())
ox = []
for i in range(n):
    ox.append(input().rstrip())

for j in ox:
    score = 0
    cnt = 0
    for i in j:
        if i == 'O':
            cnt += 1
            score += cnt
        elif i == 'X':
            cnt = 0
    print(score)