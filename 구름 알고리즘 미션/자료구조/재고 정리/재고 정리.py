N = int(input())

stored = {}
for _ in range(N):
	S, A = map(str, input().split(" "))
	if S not in stored:
		stored[S] = int(A)
	else:
		stored[S] += int(A)

result = sorted(stored.items())
for S, A in result:
	print(S, A)
	