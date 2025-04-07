const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	
	for await (const line of rl) {
		input.push(line);
		if(input.length === 2) rl.close();
	}
	
	let N = +input[0];
	let As = input[1].split(" ").map(n => +n);
	
	let result = 2*N + As[0] + As[As.length -1];
	for(let i = 0 ; i < N-1 ; i++){
		result += Math.abs(As[i] - As[i+1]);
	}
	
	console.log(result);
	process.exit();
})();
