from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)
    
    distance = [0] * (n + 1)
    visited = [False] * (n + 1)
    q = deque([1])
    visited[1] = True
    
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                distance[next] = distance[cur] + 1
                q.append(next)
    maxDistance = max(distance)
    return distance.count(maxDistance)
                
        