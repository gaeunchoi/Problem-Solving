function solution(topping) {
    let result = 0;
    
    const left = new Set();
    const right = {};
    let rightCnt = 0;
    
    for(const t of topping){
        if(!right[t]) rightCnt++;
        right[t] = (right[t] || 0) + 1;
    }
    
    for(const t of topping){
        left.add(t);
        
        right[t]--;
        if(right[t] === 0) rightCnt--;
        if(left.size === rightCnt) result++;
    }
    return result;
}