function solution(n, results) {
    const winGraph = Array.from({length: n+1}, () => []);
    const loseGraph = Array.from({length: n+1}, () => []);
    
    for(const [s, e] of results){
        winGraph[s].push(e);
        loseGraph[e].push(s);
    }
    
    const BFS = (s, graph) => {
        const visited = Array(n+1).fill(false);
        visited[s] = true;
        const q = [s];
        let head = 0;
        let cnt = 0;
        
        while(head < q.length){
            const cur = q[head++];
            for(const next of graph[cur]){
                if(!visited[next]){
                    visited[next] = true;
                    q.push(next);
                    cnt++;
                }
            }
        }
        return cnt;
    }
    
    let answer = 0;
    for(let i = 1 ; i <= n ; i++){
        const win = BFS(i, winGraph);
        const lose = BFS(i, loseGraph);
        if(win + lose === n-1) answer++;
    }
    return answer;
}