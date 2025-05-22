function solution(begin, target, words){
    let head = 0;
    const q = [[begin, 0]];
    const visited = new Set([begin]);
    
    const isOneLetterDiff = (a, b) => {
        let cnt = 0;
        for(let i = 0 ; i < a.length ; i++){
            if(a[i] !== b[i]) cnt++;
        }
        return cnt === 1;
    }
    
    while(head < q.length){
        const [cur, step] = q[head++];
        
        if(cur === target) return step;
        
        for(const word of words){
            if(isOneLetterDiff(cur, word) && !visited.has(word)){
                visited.add(word);
                q.push([word, step + 1]);
            }
        }
    }
    
    return 0;
}