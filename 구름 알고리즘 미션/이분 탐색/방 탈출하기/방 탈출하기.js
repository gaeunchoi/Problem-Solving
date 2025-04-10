// Run by Node.js
const readline = require('readline');

const rl = readline.createInterface({ input: process.stdin });

const input = [];
rl.on('line', (line) => {
	input.push(line.trim());
}).on('close', () => {
	const N = Number(input[0]);
	const A = input[1].split(' ').map(Number).sort((a, b) => a - b);
	const M = Number(input[2]);
	const B_list = input.slice(3, 3 + M).map(Number);  // 중요!!

	const isInclude = (target) => {
		let left = 0;
		let right = N - 1;

		while (left <= right) {
			const mid = Math.floor((left + right) / 2);
			if (A[mid] === target) return true;
			else if (A[mid] < target) left = mid + 1;
			else right = mid - 1;
		}
		return false;
	};

	const output = [];
	for (let b of B_list) {
		output.push(isInclude(b) ? '1' : '0');
	}
	console.log(output.join('\n'));
});
