function solution(begin, target, words) {
    const visited = {[begin]: 0};
    const queue = [begin];
    
    while(queue.length){
        const cur = queue.shift();
        if(cur === target) break;
        
        for(let w of words){
            if(isOneLetterDiff(w, cur) && !visited[w]){
                visited[w] = visited[cur] + 1;
                queue.push(w);
            }
        }
    }
    
    return visited[target] ? visited[target] : 0;
}

const isOneLetterDiff = (a, b) => {
    let cnt = 0;
    const len = a.length;
    
    for(let i = 0 ; i < len ; i++){
        if(a[i] !== b[i]) cnt++;
    }
    
    return cnt === 1 ? true : false;
}