const INF = Infinity;

function solution(N, road, K) {
    const adjList = Array.from({length: N+1}, () => []);
    
    for(let [a, b, c] of road){
        adjList[a].push([b, c]);
        adjList[b].push([a, c]);
    }
    
    const dist = Array(N+1).fill(INF);
    dist[1] = 0;
    
    const queue = [[1, 0]];
    while(queue.length) {
        const [current, currentDist] = queue.pop();
        
        if(dist[current] < currentDist) continue;
        
        for(let [next, time] of adjList[current]){
            const nextDist = currentDist + time;
            if(nextDist < dist[next]){
                dist[next] = nextDist;
                queue.push([next, nextDist]);
            }
        }
        
        queue.sort((a, b) => b[1] - a[1]);
    }
    
    return dist.filter(t => t <= K).length;
    
}