num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

n, b = input().split()
n = ''.join(reversed(n))
b = int(b)

result = 0
for x in range(len(n)):
    sum = num.index(n[x]) * (b ** x)
    result += sum

print(result)
