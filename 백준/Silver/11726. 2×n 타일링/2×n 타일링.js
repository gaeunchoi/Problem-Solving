const file = process.platform === 'linux' ? 0 : './input.txt';
const input = require("fs").readFileSync(file).toString().trim("");

function dpMemo(n) {
    let memo = new Array(n+1).fill(0);

    function dp(n){
        if(memo[n] !== 0) return memo[n];

        if(n === 1 || n === 2) memo[n] = n;
        else memo[n] = (dp(n-1) + dp(n-2)) % 10007;

        return memo[n];
    }

    return dp(n);
}

const result = dpMemo(Number(input));
console.log(result);