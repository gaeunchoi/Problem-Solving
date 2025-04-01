def primeNum(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

M = int(input())
N = int(input())

cnt = 0
min = N
for i in range(M, N+1):
    if primeNum(i) == True:
        cnt += i
        if i < min:
            min = i

if cnt == 0:
    print(-1)
else:
    print(cnt)
    print(min)
