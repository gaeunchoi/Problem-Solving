const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const bfs = (language) => {
	let q = [];
	let head = 0;
	q.push(0);
	
	visited = Array(N).fill(false);
	visited[0] = true;
	
	while(head < q.length){
		country = q[head++];
		for(const oc of graph[country]){
			if(!visited[oc] && (a[oc] === a[0] || a[oc] === language)){
				visited[oc] = true;
				q.push(oc);
			}
		}
	}
	
	let visitCnt = 0;
	for(let i = 0 ; i < N ; i++){
		if(visited[i]) visitCnt++;
	}
	return visitCnt;
}

const [N, M] = input[0].split(" ").map(Number);
const a = input[1].split(" ").map(Number);
const graph = Array.from({length: N}, () => []);

for(let i = 2 ; i <= M+1 ; i++){
	const [p, q] = input[i].split(" ").map(Number);
	graph[p-1].push(q-1);
	graph[q-1].push(p-1);
}

let result = 0;
for(let i = 1 ; i <= 10 ; i++){
	if(a[0] != i){
		result = Math.max(result, bfs(i));
	}
}

console.log(result);