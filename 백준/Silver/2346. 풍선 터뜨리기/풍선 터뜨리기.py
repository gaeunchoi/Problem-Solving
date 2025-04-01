from collections import deque

N = int(input())
poong = list(map(int, input().split()))
q = deque(enumerate(poong))

result = []

while q:
    idx, movement = q.popleft()
    result.append(idx + 1)

    if movement > 0:
        q.rotate(-(movement -1))
    elif movement < 0:
        q.rotate(-movement)

print(*result)