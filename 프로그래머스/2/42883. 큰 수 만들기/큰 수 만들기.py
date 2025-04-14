def solution(number, k):
    stack = []
    removeCnt = k
    
    for i, v in enumerate(number):
        while removeCnt > 0 and len(stack) > 0 and stack[-1] < v:
            stack.pop()
            removeCnt -= 1
        
        stack.append(v)
        
    
    while removeCnt > 0:
        stack.pop()
        removeCnt -= 1
        
    return "".join(stack)