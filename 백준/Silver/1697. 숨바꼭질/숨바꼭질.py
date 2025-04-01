from collections import deque
N, K = map(int, input().split())
dis = [0] * 100001

q = deque()
q.append(N)

while q:
    c_pos = q.popleft()
    if c_pos == K:
        print(dis[c_pos])
        break
    for move_pos in (c_pos-1, c_pos+1, 2 * c_pos):
        if 0 <= move_pos < 100001 and not dis[move_pos]:
            dis[move_pos] = dis[c_pos] + 1
            q.append(move_pos)