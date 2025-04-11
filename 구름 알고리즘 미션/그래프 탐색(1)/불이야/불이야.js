const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const directions = [[-1, 0], [0, -1], [1, 0], [0, 1]];
const [R, C] = input[0].split(" ").map(Number);
const lab = Array.from({length: R}, () => Array(C).fill(0));
for(let i = 1 ; i <= R ; i++){
	lab[i-1] = input[i].split("");
}

const bfs = () => {
	let visited = Array.from({length: R}, () => Array(C).fill(false));
	let distance = Array.from({length: R}, () => Array(C).fill(0));
	let q = [];
	let head = 0;
	
	for(let i = 0 ; i < R ; i++){
		for(let j = 0 ; j < C ; j++){
			if(lab[i][j] === '@') {
				q.push([i, j]);
				visited[i][j] = true;
			}
		}
	}
	
	while(head < q.length){
		const [cx, cy] = q[head++];
		for(const [dx, dy] of directions){
			const [mx, my] = [cx + dx, cy + dy];
			if(0 <= mx && mx < R && 0 <= my && my < C && lab[mx][my] !== '#' && !visited[mx][my]){
				q.push([mx, my]);
				visited[mx][my] = true;
				distance[mx][my] = distance[cx][cy] + 1;
			}
		}
	}
	
	return [distance, visited];
}

const [dist, visited] = bfs();
for(let i = 0 ; i < R ; i++){
	for(let j = 0 ; j < C ; j++){
		if(lab[i][j] === '&'){
			console.log(visited[i][j] ? dist[i][j] - 1 : -1);
		}
	}
}