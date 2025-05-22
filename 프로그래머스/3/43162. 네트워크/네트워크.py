def solution(n, computers):
    visited = [False] * n
    result = 0
    
    def DFS(com):
        visited[com] = True
        
        for i in range(n):
            if not visited[i] and computers[com][i] == 1:
                DFS(i)
    
    for i in range(n):
        if not visited[i]:
            DFS(i)
            result += 1
    return result
        