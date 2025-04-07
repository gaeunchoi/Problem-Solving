N = int(input())
maxP, minP = 0, 100000
maxN, minN = "", ""
for _ in range(N):
	S, P = input().split(" ")
	if maxP < int(P):
		maxP = int(P)
		maxN = S
	if minP > int(P):
		minP = int(P)
		minN = S

print(maxN, maxP)
print(minN, minP)