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
	const mountains = input[1].split(" ").map(Number);
	
	let result = [];
	let stack = [];
	for(let i = 0 ; i < N ; i++){
		process.stdout.write(stack.length + " ");
		
		while(stack.length > 0 && mountains[stack[stack.length - 1]] <= mountains[i]) {
			stack.pop();
		}
		
		stack.push(i);
	}
	process.exit();
})();
