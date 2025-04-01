import sys

N = int(sys.stdin.readline())

times = list(map(int, sys.stdin.readline().split()))

times.sort()

acc = 0
for i in range(N):
    acc += times[i]
    times[i] = acc

print(sum(times))