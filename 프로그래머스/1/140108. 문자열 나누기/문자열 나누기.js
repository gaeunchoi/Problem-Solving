function solution(s) {
    let answer = 0;
    let q = s.split("");
    
    while(q.length > 0){
        let a = 1, b = 0;
        let x = q.shift();
        
        while(q.length > 0){
            let n = q.shift();
            
            if(n === x) a++;
            else b++;
            
            if(a === b){
                answer++;
                break;
            }
        }
        if(a !== b && q.length === 0) answer++;
    }
    return answer;
    
}