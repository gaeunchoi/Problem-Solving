// Run by Node.js
const readline = require('readline');

const rl = readline.createInterface({ input: process.stdin });

const input = [];

rl.on('line', function (line) {
	input.push(line);
}).on('close', function () {
	const [N, K] = input[0].split(" ").map(Number);
	const board = [];
	for(let i = 1 ; i <= N ; i++){
		board.push(input[i].split(" ").map(Number));
	}
	const directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]];
	
	let cnt = 0;
	for(let x = 0 ; x < N ; x++){
		for(let y = 0 ; y < N ; y++){
			if(board[x][y] === 0){
				let clouds = 0;
				for(const [dx, dy] of directions){
					const [mx, my] = [x + dx, y + dy];
					if(0 <= mx && mx < N && 0 <= my && my < N && board[mx][my] === 1) clouds++;
				}
				if(clouds === K) cnt++;
			}
		}
	}
	
	console.log(cnt);
	process.exit();
});
