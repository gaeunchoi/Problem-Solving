N = int(input())

cnt = 0

while N >= 0:
    if N % 5 == 0:
        cnt += N // 5
        print(cnt)
        break
    N -= 3      # 5의 배수가 될 때 까지 -3하면서 cnt +1
    cnt += 1
else:
    print(-1)