N = int(input())

cnt = 0
while N:
	N //= 5
	cnt += N

print(cnt)