def rotate(mat):
    n = len(mat)
    m = len(mat[0])
    result = [[-1] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = mat[i][j]
    return result

def check_center(mat):
    n = len(mat) // 3
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            if mat[i][j] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    for rotation in range(4):
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                if check_center(new_lock) == True:
                    return True

                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
        key = rotate(key)
    return False