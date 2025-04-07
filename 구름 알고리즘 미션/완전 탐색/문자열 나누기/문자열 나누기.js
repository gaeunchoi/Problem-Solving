// Run by Node.js
const readline = require('readline');

const rl = readline.createInterface({ input: process.stdin });

const input = [];

rl.on('line', function (line) {
	input.push(line);
}).on('close', function () {
	const N = +input[0];
	const S = input[1];
	
	let result = [];
	for(let i = 1 ; i < N-1 ; i++){
		for(let j = i+1 ; j < N ; j++){
			const p1 = S.slice(0, i);
			const p2 = S.slice(i, j);
			const p3 = S.slice(j);
			result.push([p1, p2, p3]);
		}
	}
	
	let flat = [];
	for(let r of result) flat.push(...r);
	const P = [...new Set(flat)].sort();
	
	let maxScore = 0;
	result.forEach(([p1, p2, p3]) => {
		let i = P.indexOf(p1), j = P.indexOf(p2), k = P.indexOf(p3);
		const score = i + j + k + 3;
		maxScore = score > maxScore ? score : maxScore;
	})
	
	console.log(maxScore);
	process.exit();
});
