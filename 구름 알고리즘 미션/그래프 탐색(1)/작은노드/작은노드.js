const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M, K] = input[0].split(" ").map(Number);
const graph = Array.from({length: N+1}, () => []);
for(let i = 1 ; i <= M ; i++){
	const [s, e] = input[i].split(" ").map(Number);
	graph[s].push(e);
	graph[e].push(s);
}

for(let i = 1 ; i <= N ; i++){
	graph[i].sort((a, b) => a - b);
}

const visited = Array(N+1).fill(false);
let cnt = 0;
let lastNode = 0;

const dfs = (nodeNum) => {
	visited[nodeNum] = true;
	cnt++;
	
	for(const node of graph[nodeNum]){
		if(!visited[node]){
			dfs(node);
			return;
		}
	}
	lastNode = nodeNum;
}

dfs(K);
console.log(cnt, lastNode);