import sys

N = int(sys.stdin.readline())

conf = []
for _ in range(N):
    s, f = map(int, sys.stdin.readline().split())
    conf.append([s, f])

conf.sort(key = lambda x : x[0])
conf.sort(key = lambda x : x[1])

cnt = 0
finish_time = 0

for i, j in conf:
    if i >= finish_time:
        cnt += 1
        finish_time = j

print(cnt)