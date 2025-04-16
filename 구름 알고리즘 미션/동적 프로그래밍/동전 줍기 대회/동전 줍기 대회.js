const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = +input[0];
const coins = input[1].split(" ").map(Number);
let pickCoins = Array(N).fill(0);
pickCoins[0] = coins[0];

for(let i = 1 ; i < N ; i++){
	pickCoins[i] = Math.max(coins[i], coins[i] + pickCoins[i-1]);
}

console.log(Math.max(...pickCoins) > 0 ? Math.max(...pickCoins) : 0);