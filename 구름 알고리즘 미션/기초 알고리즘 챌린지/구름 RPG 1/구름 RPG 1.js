// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	for await (const line of rl) {
		input.push(line);
		if(input.length === +input[0] + 1) rl.close();
	}
	
	const isPrime = (n) => {
		for(let i = 2 ; i < parseInt(Math.sqrt(n)) + 1 ; i++){
			if(n % i === 0) return false;
		}
		return true;
	}
	const N = +input[0];
	for(let i = 1 ; i <= N ; i++){
		const A = +input[i];
		console.log(isPrime(A) ? "Yes" : "No");
	}
	
	process.exit();
})();
