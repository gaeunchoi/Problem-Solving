def solution(numbers):
    result = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers) - 1, -1, -1):
        current = numbers[i]
        while stack and stack[-1] <= current:
            stack.pop()
        
        if stack:
            result[i] = stack[-1]
        
        stack.append(current)
    return result