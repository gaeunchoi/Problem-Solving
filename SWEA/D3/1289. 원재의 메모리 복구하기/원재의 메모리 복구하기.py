T = int(input())

for tc in range(1, T+1):
    bits = list(map(int, input().rstrip()))
    result = [0] * len(bits)

    cnt = 0
    for i in range(len(bits)):
        if bits[i] == 0 and result[i] == 1:
            result[i:] = [0] * (len(bits) - i)
            cnt += 1
        elif bits[i] == 1 and result[i] == 0:
            result[i:] = [1] * (len(bits) - i)
            cnt += 1

    print(f'#{tc} {cnt}')
