import sys

num = int(input())

result_arr= [[0 for _ in range(101)] for _ in range(101)]

for i in range(num):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    for x in range(a, a+10):
        for y in range(b, b+10):
            result_arr[x][y] = 1

result = 0
for i in result_arr:
    result += sum(i)

print(result)