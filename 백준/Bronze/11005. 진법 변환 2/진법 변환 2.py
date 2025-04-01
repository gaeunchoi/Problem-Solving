num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n, b = map(int, input().split())

result = []
while True:
    if n < b:
        result.append(n)
        break
    result.append(n % b)
    n //= b

result.reverse()
for i in result:
    print(num[i], end = '')