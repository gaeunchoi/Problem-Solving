from collections import deque

def solution(land):
    answer = 0
    rows, cols = len(land), len(land[0])

    visited = [[False] * cols for _ in range(rows)]
    direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    oil_sizes = [0] * cols

    def check_oil_size(x, y):
      queue = deque()
      queue.append([x, y])
      visited[x][y] = True

      cnt = 1

      row_oil_here = {y}

      while queue:
        current_x, current_y = queue.popleft()
        for direction_x, direction_y in direction:
          move_x, move_y = current_x + direction_x, current_y + direction_y
          if 0 <= move_x < rows and 0 <= move_y < cols:
            if land[move_x][move_y] == 1 and not visited[move_x][move_y]:
              queue.append([move_x, move_y])
              visited[move_x][move_y] = True
              cnt += 1
              row_oil_here.add(move_y)
      
      for i in row_oil_here:
        oil_sizes[i] += cnt
                  
    for i in range(rows):
        for j in range(cols):
          if land[i][j] == 1 and not visited[i][j]:
            check_oil_size(i, j)
      
    answer = max(oil_sizes)
    return answer