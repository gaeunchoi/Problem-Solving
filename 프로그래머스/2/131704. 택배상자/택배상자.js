function solution(order) {
    let stack = [];
    let idx = 0;
    let box = 1;
    
    while(box <= order.length){
        if(box === order[idx]){
            idx++;
        } else {
            stack.push(box);
        }
        box++;
        
        while(stack.length > 0 && stack[stack.length - 1] === order[idx]){
            stack.pop();
            idx++;
        }
    }
    return idx;
}