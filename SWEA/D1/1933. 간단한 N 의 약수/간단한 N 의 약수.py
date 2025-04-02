N = int(input())
result = []
for i in range(1, N//2 + 1):
    if N % i == 0 :
        result.append(i)
result.append(N)
print(*result)