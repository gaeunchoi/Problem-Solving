n = int(input())
result = 0

for i in range(1, n+1):
    num = list(map(int, str(i)))
    s = i + sum(num)
    if s == n:
        result = i
        break

print(result)