def check(park, H, W, a, b):
    if 0 <= a < H and 0 <= b < W:
        if park[a][b] == 'X':
            return False
        else:
            return True
    return False

def solution(park, routes):
    H, W = len(park), len(park[0])

    cx, cy = 0, 0
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                cx, cy = i, j

    for route in routes:
        direction, distance = map(str, route.split())
        mx, my = cx, cy
        if direction == 'N':
            mx = cx - int(distance)
        elif direction == 'S':
            mx = cx + int(distance)
        elif direction == 'W':
            my = cy - int(distance)
        else:
            my = cy + int(distance)

        gogo = True
        for i in range(min(cx, mx), max(cx, mx) + 1):
            if not gogo:
                break

            for j in range(min(cy, my), max(cy, my) + 1):
                if not check(park, H, W, i, j):
                    gogo = False
                    break
                else:
                    gogo = True

        if gogo:
            cx, cy = mx, my

    return [cx, cy]

print(solution(["SOO","OXX","OOO"], ["E 2","S 2","W 1"]	))
print(solution(["OSO","OOO","OXO","OOO"],["E 2","S 3","W 1"]		))