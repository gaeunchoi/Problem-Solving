def prime_list():       # 에라토스테네스의 체로 소수 리스트 구하기
    n = 10001           # 문제에서 제시한 조건
    sieve = [True] * n

    for i in range(2, int(n ** 0.5)):
        if sieve[i]:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]


T = int(input())

listPrime = prime_list()

for i in range(T):
    n = int(input())

    a = 0
    b = 0

    for i in range(len(listPrime)):
        if listPrime[i] >= n / 2:
            if n - listPrime[i] in listPrime:
                a = listPrime[i]
                b = n - listPrime[i]
                break
    print(b, a)
