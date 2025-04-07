// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	
	for await (const line of rl) {
		input.push(line);
		if(input.length === input[0]+1) rl.close();
	}
	
	function isPrime(n){
		if(n < 2) return false;
		
		for(let i = 2 ; i < parseInt(n ** 0.5) + 1 ; i++){
			if(n % i === 0) return false;
		}
		
		return true;
	}
	
	const N = +input[0];
	for(let i = 1; i <= N ; i++){
		let result = 0;
		const val = input[i];
		while(!isPrime(val - result)) result++;
		console.log(result);
	}
	
	process.exit();
})();
