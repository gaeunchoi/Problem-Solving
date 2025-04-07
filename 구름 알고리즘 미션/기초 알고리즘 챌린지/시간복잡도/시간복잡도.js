// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	
	for await (const line of rl) {
		input.push(line);
		rl.close();
	}

	let N = +input[0]
	let cnt = 0;
	while(+N > 0){
		N = Math.floor(N/5);
		cnt += N;
	}
	
	console.log(cnt);
	process.exit();
})();
