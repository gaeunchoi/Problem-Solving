const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let input = [];
rl.on('line', line => {
  input.push(line.trim());
}).on('close', () => {
	
	const find = (u) => {
		if(parent[u] !== u) parent[u] = find(parent[u]);
		return parent[u];
	}
	
	const union = (u, v) => {
		const rootU = find(u);
		const rootV = find(v);
		
		if(rootU === rootV) return false;
		if(rootU < rootV) parent[rootV] = rootU;
		else parent[rootU] = rootV;
		return true;
	}
	
  const [N, M] = input[0].split(' ').map(Number);
  const parent = Array.from({ length: N + 1 }, (_, i) => i);
	let cnt = N;
	
	for(let i = 1; i <= M ; i++){
		const [a, b] = input[i].split(' ').map(Number);
		if(union(a, b)) cnt--;
	}
	
	console.log(cnt);
	
});
