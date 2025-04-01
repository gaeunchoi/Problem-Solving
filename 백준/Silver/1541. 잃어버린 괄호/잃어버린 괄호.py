import sys

susik = list(sys.stdin.readline().rstrip().split("-"))

result = []
for i in susik:
    cnt = 0

    nums = list(map(int, i.split("+")))

    for j in nums:
        cnt += j

    result.append(int(cnt))

n = result[0]
for i in range(1, len(result)):
    n -= result[i]

print(n)