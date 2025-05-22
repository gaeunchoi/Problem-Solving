function solution(n, computers) {
    let visited = new Array(n).fill(false);
    let result = 0;
    
    const DFS = (com) => {
        visited[com] = true;
        
        for(let i = 0 ; i < n ; i ++){
            if(computers[com][i] === 1 && !visited[i]) DFS(i);
        }
    }
     
    for(let i = 0 ; i < n ; i++){
        if(!visited[i]){
            DFS(i);
            result++;
        }
    }
    return result;
}