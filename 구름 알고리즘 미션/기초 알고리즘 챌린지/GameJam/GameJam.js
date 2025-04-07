// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	for await (const line of rl) {
		input.push(line);
		if(input.length === input[0] + 3) rl.close();
	}
	
	function playGame(cx, cy, N){
		let x = cx, y = cy;
		let visited = Array.from({length: N}, () => Array(N).fill(false));
		visited[x][y] = true;
		
		let result = 1;
		let flag = true;
		
		while(flag){
			const [mx, my] = cmd[x][y];
			const moveSteps = moveCnt[x][y];
			for(let i = 0 ; i < moveSteps ; i++){
				x = (x + mx + N) % N;
				y = (y + my + N) % N;
				
				if(visited[x][y]){
					flag = false;
					break;
				}
				
				visited[x][y] = true;
				result++;
			}
		}
		return result;
	}
	
	const N = +input[0];
	const [Rg, Cg] = input[1].split(" ").map((v) => +v - 1);
	const [Rp, Cp] = input[2].split(" ").map((v) => +v - 1);
	const directions = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]};
	const order = input.slice(3, 3 + N).map(v => v.split(" "));
	const moveCnt = Array.from({length: N}, () => Array(N).fill(0));
	const cmd = Array.from({length: N}, () => Array(N).fill(null));
	
	for(let i = 0 ; i < N ; i++){
		for(let j = 0 ; j < N ; j++){
			const elem = order[i][j];
			const s = parseInt(elem.slice(0, -1));
			const c = elem.slice(-1);
			moveCnt[i][j] = s
			cmd[i][j] = directions[c];
		}
	}
	
	const goormScore = playGame(Rg, Cg, N);
	const playerScore = playGame(Rp, Cp, N);
	
	if (goormScore > playerScore) {
	console.log("goorm", goormScore);
	} else {
	console.log("player", playerScore);
	}
	
	process.exit();
})();
