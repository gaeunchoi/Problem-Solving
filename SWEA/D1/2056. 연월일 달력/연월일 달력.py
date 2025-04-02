days = {1: 31, 2: 28, 3:31, 4:30, 5:31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
T = int(input())

for test_case in range(1, T+1):
    result = ''
    full = str(input())
    y = full[0:4]
    m = full[4:6]
    d = full[6:8]

    if 1 <= int(m) <= 12 and 1 <= int(d) <= days[int(m)]:
        result = y + '/' + m + '/' + d
    else:
        result += '-1'

    print(f'#{test_case} {result}')

