def solution(arr):
    def compress(x, y, size):
        first = arr[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != first:
                    half = size // 2
                    res1 = compress(x, y, half)
                    res2 = compress(x, y + half, half)
                    res3 = compress(x + half, y, half)
                    res4 = compress(x + half, y + half, half)
                    return [sum(x) for x in zip(res1, res2, res3, res4)]
        return [1, 0] if first == 0 else [0, 1]
    return compress(0, 0, len(arr))