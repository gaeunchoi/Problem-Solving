N = int(input())
Alice = list(map(int, input().split(" ")))
Bob = list(map(int, input().split(" ")))

scores = [0, 0]
for i in range(len(Alice)):
	if Alice[i] == Bob[i]:
		scores[0] += 1
		scores[1] += 1
	elif Alice[i] > Bob[i]:
		if Alice[i] - Bob[i] == 7:
			scores[0] -= 1
			scores[1] += 3
		else:
			scores[0] += 2
	else:
		if Bob[i] - Alice[i] == 7:
			scores[0] += 3
			scores[1] -= 1
		else:
			scores[1] += 2
			
print(scores[0], scores[1])	