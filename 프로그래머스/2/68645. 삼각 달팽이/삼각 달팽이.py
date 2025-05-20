def solution(n):
    arr = [[0] * i for i in range(1, n+1)]
    directions = [[1, 0], [0, 1], [-1, -1]] # 아래, 오른쪽, 왼쪽위(좌측 대각선 위)
    turn = 0
    x, y = 0, 0
    i = 1
    end_num = sum(i for i in range(1, n+1))
    
    while i <= end_num:
        arr[x][y] = i
        i += 1
        mx, my = x + directions[turn][0], y + directions[turn][1]
        
        if 0 <= mx < n and 0 <= my < n and arr[mx][my] == 0:
            x, y = mx, my
        else:
            turn = (turn + 1) % 3
            x += directions[turn][0]
            y += directions[turn][1]
     
    answer = []
    for row in arr:
        for item in row:
            answer.append(item)
    return answer
    