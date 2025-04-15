function solution(maps) {
    const N = maps.length;
    const M = maps[0].length;
    const directions = [[-1, 0], [0, -1], [1, 0], [0, 1]];

    let S, L, E;
    for(let i = 0 ; i < N ; i++){
        for(let j = 0 ; j < M ; j++){
            if(maps[i][j] === 'S') S = [i, j];
            else if(maps[i][j] === 'L') L = [i, j];
            else if(maps[i][j] === 'E') E = [i, j];
        }
    }
    
    const bfs = (s, e) => {
        const visited = Array.from({length: N}, () => Array(M).fill(false));
        visited[s[0]][s[1]] = true;
        const q = [[...s, 0]];
        let head = 0;
        
        while(head < q.length){
            const [x, y, dist] = q[head++];
            if(x === e[0] && y === e[1]) return dist;
            
            for(const [dx, dy] of directions){
                const [mx, my] = [x + dx, y + dy];
                if(0 <= mx && mx < N && 0 <= my && my < M && !visited[mx][my] && maps[mx][my] !== 'X'){
                    visited[mx][my] = true;
                    q.push([mx, my, dist+1]);
                }
            }
        }
        return -1;
    };
    
    const StoL = bfs(S, L);
    const LtoE = bfs(L, E);
    if(StoL === -1 || LtoE === -1) return -1;
    return StoL + LtoE;
}