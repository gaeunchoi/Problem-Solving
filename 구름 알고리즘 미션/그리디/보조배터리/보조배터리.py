import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
N = int(input())
charger = [tuple(map(int, input().split())) for _ in range(N)]

charger.sort()

cnt, cash = 0, 0

for c, t in charger:
    if t == 0:  # X 타입
        if A > 0:
            A -= 1
        elif C > 0:
            C -= 1
        else:
            continue
    else:  # Y 타입
        if B > 0:
            B -= 1
        elif C > 0:
            C -= 1
        else:
            continue

    cnt += 1
    cash += c

print(cnt, cash)
