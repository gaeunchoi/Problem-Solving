// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	
	for await (const line of rl) {
		input.push(line);
		if(input.length === 4) rl.close();
	}
	
	const [N, M, Xs] = input[0].split(" ").map(Number);
	let H = input[1].split(" ").map(Number);
	const Q = +input[2];
	const D = input[3].split(" ");
	
	let result = 0;
	let pos = Xs - 1;
	
	for(let i = 0 ; i < Q ; i++){
		if(H[pos] + i >= M){
			result += H[pos] + i;
			H[pos] -= H[pos] + i;
		}
		
		if(D[i] === 'L') pos = (pos-1 + N) % N;
		else if(D[i] === 'R') pos = (pos+1) % N;
	}
	
	console.log(result);
	
	process.exit();
})();
