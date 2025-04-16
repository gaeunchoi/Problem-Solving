const MOD = (10**9) + 7;
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = +input[0];
const dp = Array(N+1).fill(0);

dp[1] = 0;
dp[2] = 1;

for(let i = 3 ; i <= N ; i++){
	dp[i] = (dp[i-1] + dp[i-2]) % MOD;
}

console.log(dp[N]);