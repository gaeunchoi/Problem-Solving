def solution(order):
    idx = 0
    box = 1
    stack = []
    while box <= len(order):
        if box == order[idx]:
            idx += 1
        else:
            stack.append(box);
        box += 1
        
        while stack and stack[-1] == order[idx]:
            stack.pop()
            idx += 1
    return idx
        