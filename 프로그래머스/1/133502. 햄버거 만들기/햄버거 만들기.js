function solution(ingredient) {
    const hamburger = [1, 2, 3];
    
    let stack = [];
    let cnt = 0;
    for(const food of ingredient){
        stack.push(food);
        if(stack.length >= 4 && stack.slice(-4).join("") === "1231"){
            cnt++;
            stack.splice(-4);
        }
    }
    return cnt;
}