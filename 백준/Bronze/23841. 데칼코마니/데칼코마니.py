n, m = map(int, input().split())

color = []
for i in range(n):
    color = list(input())
    for j in range(m):
        if color[j] != '.':
            color[-(j+1)] = color[j]
    print(''.join(color))