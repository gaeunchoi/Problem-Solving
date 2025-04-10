// Run by Node.js
const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin });

const input = [];

rl.on('line', line => input.push(line)).on('close', () => {
	const N = Number(input[0]);
	const S = input[1].split(' ').map(Number).sort((a, b) => a - b);
	
	const bisectRight = (arr, target) => {
		let left = 0;
		let right = arr.length;
		while(left < right){
			let mid = Math.floor((left + right) / 2);
			if(arr[mid] <= target) left = mid + 1;
			else right = mid;
		}
		return left;
	}
	
	let answer = 0;
	for(let i = 0 ; i < N-2 ; i++){
		for(let j = i+1 ; j < N-1 ; j++){
			const target = S[i] + S[j];
			const idx = bisectRight(S, target) - 1;
			answer += idx > j ? idx - j : 0;
		}
	}
	console.log(answer);
	process.exit();
});
