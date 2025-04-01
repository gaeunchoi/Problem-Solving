def primeNum(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

N = int(input())

num = list(map(int, input().split()))
cnt = 0

for i in range(N):
    if primeNum(num[i]) == True:
        cnt += 1

print(cnt)