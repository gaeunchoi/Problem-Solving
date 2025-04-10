// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let M = 0, N = 0;
	for await (const line of rl) {
		[N, M] = line.split(" ").map(Number);
		rl.close();
	}
	
	current = Math.floor(M * 100 / N);
	goal = current + 1;
	
	let minK = 1000000000000;
	let left = 1;
	let right = minK - 1;
	
	while(left <= right){
		let mid = Math.floor((left + right) / 2);
		let winRate = Math.floor((M + mid) * 100 / (N + mid));
		if(winRate >= goal){
			minK = mid;
			right = mid - 1;
		} else {
			left = mid + 1;
		}
	}
	
	console.log(minK === 1000000000000 ? 'X' : minK);
	
	process.exit();
})();
