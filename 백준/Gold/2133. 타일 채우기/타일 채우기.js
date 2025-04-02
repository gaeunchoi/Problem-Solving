const file = process.platform === 'linux' ? 0 : './input.txt';
const N = require("fs").readFileSync(file).toString().trim("");

function dpMemo(n){
    let memo = new Array(n+1).fill(0);
    memo[1] = 0;
    memo[2] = 3;
    
    for(let i = 4 ; i <= N ; i += 2){
        memo[i] = memo[i-2] * 3 + 2;
        
        for(let j = i - 4; j  >= 0 ; j -= 2){
            memo[i] += memo[j] * 2;
        }
    }
    return memo[n];
}

const result = dpMemo(Number(N));
console.log(result);