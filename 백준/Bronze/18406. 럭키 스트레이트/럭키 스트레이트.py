import sys
input = sys.stdin.readline

N = list(map(int, input().rstrip()))
length = len(N) // 2
l, r = N[:length], N[length:]

left, right = 0, 0
for i in range(length):
    left += l[i] % 10
    right += r[i] % 10

print('LUCKY' if left == right else 'READY')