def fact(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    bridge = fact(b) // (fact(a) * fact(b-a))
    print(bridge)