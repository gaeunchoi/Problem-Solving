a, b = map(int, input().split())
map = list()

for i in range(a):
    map.append(input())

repaint = list()


for i in range(a-7):
    for j in range(b-7):
        first_W = 0
        first_B = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if map[k][l] != 'W':
                        first_W += 1
                    if map[k][l] != 'B':
                        first_B += 1

                else:
                    if map[k][l] != 'W':
                        first_B += 1
                    if map[k][l] != 'B':
                        first_W += 1

        repaint.append(first_W)
        repaint.append(first_B)

print(min(repaint))
