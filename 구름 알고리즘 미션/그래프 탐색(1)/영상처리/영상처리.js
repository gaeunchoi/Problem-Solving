const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M] = input[0].split(" ").map(Number);
const picture = Array.from({length: M}, () => []);
const visited = Array.from({length: M}, () => Array(N).fill(false));
const directions = [[-1, 0], [0, -1], [1, 0], [0, 1]];
for(let i = 1 ; i <= M ; i++){
	picture[i-1] = input[i].split("");
}

const bfs = (x, y) => {
	let extent = 1;
	visited[x][y] = true;
	let q = [[x, y]];
	
	while(q.length > 0){
		const [cx, cy] = q.shift();
		for(const [dx, dy] of directions){
			const [mx, my] = [cx+dx, cy+dy];
			if(0 <= mx && mx < M && 0 <= my && my < N && picture[mx][my] === '#' && visited[mx][my] === false){
				q.push([mx, my]);
				visited[mx][my] = true;
				extent++;
			}
		}
	}
	
	return extent
}

let cnt = 0;
let maxBlockSize = 0;
for(let i = 0 ; i < M ; i++){
	for(let j = 0 ; j < N; j++){
		if(picture[i][j] === '#' && visited[i][j] === false){
			cnt++;
			maxBlockSize = Math.max(maxBlockSize, bfs(i, j));
		}
	}
}

console.log(cnt);
console.log(maxBlockSize);
