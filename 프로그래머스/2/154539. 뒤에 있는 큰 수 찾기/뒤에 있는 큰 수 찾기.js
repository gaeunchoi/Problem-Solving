function solution(numbers) {
    const result = new Array(numbers.length).fill(-1);
    const stack = [];
    
    for(let i = numbers.length - 1; i >= 0 ; i--){
        const current = numbers[i];
        
        while(stack.length > 0 && stack[stack.length - 1] <= current) stack.pop();
        
        if(stack.length > 0){
            result[i] = stack[stack.length - 1];
        }
        
        stack.push(current);
    }
    return result;
}