# 최상단의 위치를 찾을 필요가 없고 0이 아닐때까지 반복문을 돌면 된다 오메
def solution(board, moves):
    N = len(board)
    stack = []
    result = 0
    for move in moves:
        for j in range(N):
            curVal = board[j][move-1]
            if curVal != 0:
                if stack and stack[-1] == curVal:
                    result += 2
                    stack.pop()
                else:
                    stack.append(curVal)
                board[j][move-1] = 0
                break
    return result