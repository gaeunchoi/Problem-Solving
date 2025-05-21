from collections import defaultdict, deque
def solution(n, results):
    win_graph = defaultdict(list)
    lose_graph = defaultdict(list)
    
    for s, e in results:
        win_graph[s].append(e)
        lose_graph[e].append(s)
        
    def bfs(s, graph):
        visited = [False] * (n+1)
        q = deque([s])
        visited[s] = True
        cnt = 0
        
        while q:
            cur = q.popleft()
            for next in graph[cur]:
                if not visited[next]:
                    visited[next] = True                    
                    q.append(next)
                    cnt += 1
        return cnt
    
    answer = 0
    for i in range(1, n+1):
        win = bfs(i, win_graph)
        lose = bfs(i, lose_graph)
        if win + lose == n - 1:
            answer += 1
    return answer