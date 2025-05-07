const isValid = (s) => {
    let stack = [];
    const bracketMap = {')': '(', ']': '[', '}': '{'};
    
    for(const ch of s){
        if('([{'.includes(ch)) stack.push(ch)
        else {
            if(stack.length === 0 || stack[stack.length - 1] !== bracketMap[ch]) return false;
            stack.pop();
        }
    }
    return stack.length === 0;
}

function solution(s) {
    let cnt = 0;
    for(let i = 0 ; i < s.length ; i++){
        const rotated = s.slice(i) + s.slice(0, i);
        if(isValid(rotated)) cnt++;
    }
    return cnt;
}