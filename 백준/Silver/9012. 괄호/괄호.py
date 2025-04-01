import sys
T = int(input())

for _ in range(T):
    sum = 0
    gualho = list(sys.stdin.readline())

    for i in gualho:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1

        if sum < 0:
            print('NO')
            break

    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')