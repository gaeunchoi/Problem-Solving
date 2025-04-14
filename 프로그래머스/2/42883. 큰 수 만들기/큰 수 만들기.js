function solution(number, k) {
    const stack = [];
    let removeCnt = k;
    
    [...number].forEach((v, i) => {
        while(removeCnt > 0 && stack.length > 0 && stack[stack.length - 1] < v){
            stack.pop();
            removeCnt--;
        }
        
        stack.push(v);
    })
    
    while(removeCnt > 0){
        stack.pop();
        removeCnt--;
    }
    
    return stack.join("");
}