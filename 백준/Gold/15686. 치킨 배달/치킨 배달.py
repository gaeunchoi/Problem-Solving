import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))
            
candidates = list(combinations(chickens, M))

def get_distance(candidate):
    result = 0
    for hx, hy in houses:
        tmp = 10**9
        for cx, cy in candidate:
            tmp = min(tmp, abs(hx - cx) + abs(hy - cy))
        result += tmp
    return result

result = 10**9
for cand in candidates:
    result = min(result, get_distance(cand))
print(result)