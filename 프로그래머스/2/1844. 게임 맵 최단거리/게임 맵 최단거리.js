function solution(maps) {
    const N = maps.length, M = maps[0].length;
    const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    let visited = Array.from({length: N}, () => Array(M).fill(false));
    visited[0][0] = true;
    
    let queue = [[0, 0, 1]];
    let head = 0;
    while(head < queue.length){
        const [x, y, moveDistance] = queue[head++];
        
        if(x === N-1 && y === M-1) return moveDistance;
        
        for([dx, dy] of directions){
            const mx = x + dx, my = y + dy;
            if(0 <= mx && mx < N && 0 <= my && my < M && maps[mx][my] === 1 && !visited[mx][my]){
                visited[mx][my] = true;
                queue.push([mx, my, moveDistance + 1]);
            }
        }
    }
    
    return -1;
}