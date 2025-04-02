P, K = map(int, input().split())

result = 0
for i in range(K, P+1):
    result += 1
    if i == P:
        print(result)