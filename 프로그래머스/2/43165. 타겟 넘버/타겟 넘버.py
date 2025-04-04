def solution(numbers, target):
    result = 0

    def dfs(idx, sum):
        nonlocal result
        if idx == len(numbers):
            if sum == target:
                result += 1
            return
        
        dfs(idx+1, sum + numbers[idx])
        dfs(idx+1, sum - numbers[idx])
    
    dfs(0, 0)
    return result
