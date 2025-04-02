T = int(input())

def check_sudoku(Mat):
    for i in range(9):
        rows, cols = [0] * 10, [0] * 10

        for j in range(9):
            r = Mat[i][j]
            c = Mat[j][i]

            if rows[r] or cols[c]:
                return 0
            else:
                rows[r], cols[c] = 1, 1

            if i % 3 == 0 and j % 3 == 0:
                square = [0] * 10
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        tmp = Mat[x][y]
                        if square[tmp]:
                            return 0
                        square[tmp] = 1

    return 1

for tc in range(1, T+1):
    puzzles = [list(map(int, input().split())) for _ in range(9)]

    result = check_sudoku(puzzles)
    print(f'#{tc} {result}')