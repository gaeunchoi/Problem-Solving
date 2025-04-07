// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	
	for await (const line of rl) {
		input.push(line);
		if(input.length === 2) rl.close();
	}
	
	const N = +input[0];
	let H = input[1].split(" ").map(Number);
	
	let result = 0, cnt = 0;
	for(let i = 0 ; i < N ; i++){
		while(cnt > 0 && H[i] > 0){
			H[i] -= cnt + 1;
			cnt = (cnt+1)%4;
			result++;
		}
		
		if(H[i] <= 0) continue;
		
		const q = Math.floor(H[i] / 10);
		H[i] %= 10;
		result += 4*q;
		
		while(H[i] > 0){
			H[i] -= cnt + 1;
			cnt = (cnt+1) % 4;
			result++;
		}
	}
	
	console.log(result);
	
	process.exit();
})();
