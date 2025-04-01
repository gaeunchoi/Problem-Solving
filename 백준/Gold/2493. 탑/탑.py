import sys

N = int(sys.stdin.readline())

tower = list(map(int, input().split()))

stack = []
ans = [0] * N

for i in range(len(tower)-1, -1, -1):
    if len(stack) == 0:
        stack.append([i, tower[i]])
    else :
        while tower[i] > stack[len(stack)-1][1]:
            top = stack.pop()
            ans[top[0]] = i+1
            if len(stack) == 0:
                break

        stack.append([i, tower[i]])


for i in ans:
    print(i, end=" ")