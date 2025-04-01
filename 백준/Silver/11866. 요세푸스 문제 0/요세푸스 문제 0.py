from collections import deque
n, k = map(int, input().split())

q = deque([])

for i in range(n):
    q.append(i+1)

print("<", end='')

while q:
    for i in range(k-1):
        q.append(q[0])
        q.popleft()
    print(q.popleft(), end='')

    if q:
        print(', ', end='')
print(">")