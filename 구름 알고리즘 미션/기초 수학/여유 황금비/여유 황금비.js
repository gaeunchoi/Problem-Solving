const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	
	for await (const line of rl) {
		input.push(line);
		if(input.length === input[0] + 1) rl.close();
	}
	
	const T = input[0];
	let result = 0;
	for(let i = 1 ; i <= T ; i++){
		let [A, B] = input[i].split(" ");
		let [small, big] = +A < +B ? [+A, +B] : [+B, +A];
		if(small * 1.6 <= big && big <= small * 1.63) result++;
	}
	
	console.log(result);
	process.exit();
})();
