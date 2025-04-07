function solution(n, m, section) {
    let answer = 0;
    let idx = 0;
    while(idx < section.length){
        const start = section[idx];
        const end = start + m - 1;
        answer++;
        
        while(idx < section.length && section[idx] <= end) idx++;
    }
    
    return answer;
}