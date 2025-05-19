function solution(x, y, n) {
    let visited = new Set();
    const q = [[x, 0]];
    let head = 0;
               
    while(head < q.length){
        const [cur, cnt] = q[head++];
        
        if(cur === y) return cnt;
            
        const nextNums = [cur + n, cur * 2, cur * 3];
        for(const next of nextNums){
            if(next <= y && !visited.has(next)){
                visited.add(next);
                q.push([next, cnt + 1]);
            }
        }
    }
    return -1;
}