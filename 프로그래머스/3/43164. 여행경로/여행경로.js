function solution(tickets) {
    const graph = {};
    
    for(let [s, e] of tickets){
        if(!graph[s]) graph[s] = [];
        graph[s].push(e);
    }
    
    for(let s in graph){
        graph[s].sort();
    }
    
    const path = ["ICN"];
    const result = [];
    
    const dfs = (cur, usedCnt) => {
        if(usedCnt === tickets.length){
            result.push([...path]);
            return true;
        }
        
        const nextPath = graph[cur];
        if(!nextPath) return false;
        
        for(let i = 0 ; i < nextPath.length ; i++){
            const next = nextPath[i];
            if(next === null) continue;
            
            nextPath[i] = null;
            path.push(next);
            
            if(dfs(next, usedCnt + 1)) return true;
            
            path.pop();
            nextPath[i] = next;
        }
        
        return false;
    }
    
    dfs("ICN", 0);
    return result[0];
    
}