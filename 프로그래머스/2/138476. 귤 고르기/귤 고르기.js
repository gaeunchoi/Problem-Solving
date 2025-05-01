function solution(k, tangerine) {
    const counter = {};
    for(const size of tangerine){
        counter[size] = (counter[size] || 0) + 1;
    }
    
    const cnts = Object.values(counter).sort((a, b) => b - a);
    let total = 0, result = 0;
    for(const cnt of cnts){
        total += cnt;
        result++;
        if(total >= k) break;
    }
    return result;
}