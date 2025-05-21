function solution(n, edge) {
    let graph = Array.from({length: n+1}, () => []);
    for(const [s, e] of edge){
        graph[s].push(e);
        graph[e].push(s);
    }
    
    const distance = Array(n+1).fill(0);
    const q = [1];
    const visited = [1];
    let head = 0;
    
    while(head < q.length){
        const cur = q[head++];
        
        for(const next of graph[cur]){
            if(!visited.includes(next)){
                visited.push(next);
                distance[next] = distance[cur] + 1
                q.push(next);
            }
        }
    }
    
    const maxDistance = Math.max(...distance);
    return distance.filter(d => d === maxDistance).length;
}