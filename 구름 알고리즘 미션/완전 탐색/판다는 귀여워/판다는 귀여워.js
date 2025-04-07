// Run by Node.js
const readline = require('readline');

const rl = readline.createInterface({ input: process.stdin });

const input = [];

rl.on('line', function (line) {
	input.push(line);
}).on('close', function () {
	const [N, M, K] = input[0].split(" ").map(Number);
	const panda = [];
	for(let i = 1 ; i <= K; i++){
		const [r, c] = input[i].split(" ").map(Number);
		panda.push([r, c]);
	}
	
	let result = Infinity;
	for(let i = 1 ; i<= N ; i++){
		for(let j = 1 ; j <= M ; j++){
			if(panda.some(([r, c]) => r === i && c === j)) continue;
			
			let satis = 0;
			for(let k = 0 ; k < K; k++){
				const distance = (i - panda[k][0])**2 + (j - panda[k][1])**2
				satis += distance;
			}
			result = Math.min(result, satis);
		}
	}
	
	console.log(result)
	process.exit();
});
