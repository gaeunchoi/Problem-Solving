def find_remove_block(m, n, board):
    remove_area = set()
    
    for i in range(m-1):
        for j in range(n-1):
            cur = board[i][j]
            if not cur:
                continue
            if cur == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                remove_area.update([(i, j), (i, j+1), (i+1, j), (i+1, j+1)])    
    return list(remove_area)

def remove_block(board, positions):
    cnt = 0
    for rx, ry in positions:
        if board[rx][ry]:
            board[rx][ry] = ""
            cnt += 1
    return cnt

def apply_remove_state(m, n, board):
    for j in range(n):
        stack = []
        for i in reversed(range(m)):
            if board[i][j]:
                stack.append(board[i][j])
        for i in reversed(range(m)):
            board[i][j] = stack[m - 1 - i] if m - 1 - i < len(stack) else ""
            
def solution(m, n, board):
    arr_board = [list(row) for row in board]
    result = 0
    
    while True:
        go_remove = find_remove_block(m, n, arr_board)
        if not go_remove: 
            break
        
        removed = remove_block(arr_board, go_remove)
        result += removed
        
        apply_remove_state(m, n, arr_board)
    return result
