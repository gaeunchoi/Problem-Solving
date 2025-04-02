T = int(input())

months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for tc in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    result = 0

    if m1 == m2:
        result = d2 - d1 + 1
    else:
        result = months[m1] - d1 + 1
        for m in range(m1 + 1, m2):
            result += months[m]
        result += d2

    print(f'#{tc} {result}')