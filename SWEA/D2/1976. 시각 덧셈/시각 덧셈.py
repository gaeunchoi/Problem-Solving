T = int(input())

for tc in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    rh, rm = h1 + h2, m1 + m2
    if not 1 <= rh <= 12:
        rh -= 12
    if not 0 <= rm <= 60:
        rh += 1
        rm -= 60

    print(f'#{tc} {rh} {rm}')