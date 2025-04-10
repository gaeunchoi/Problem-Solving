N = int(input())
mountains = list(map(int, input().split()))

stack = []
for i in range(N):
	print(len(stack), end = ' ')
	while stack and mountains[stack[-1]] <= mountains[i]:
		stack.pop();
	stack.append(i)