const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = [];
rl.on("line", (line) => input.push(line.trim()))
  .on("close", () => {
	const [N, M] = input[0].split(" ").map(Number);
	const connection = Array.from({length: N+1}, () => Array(N+1).fill(false));
	for(let i = 1;  i <= M ; i++){
		const [s, e] = input[i].split(" ").map(Number);
		connection[s][e] = true;
	}
	
	const graph = Array.from({length: N+1}, () => []);
	for(let i = 1; i < N ; i++){
		for(let j = i+1 ; j < N+1; j++){
			if(connection[i][j] && connection[j][i]){
				graph[i].push(j);
				graph[j].push(i);
			}
		}
	}
	
	const visited = Array(N+1).fill(false);
	let result = 0;
	for(let i = 1 ; i < N+1 ; i++){
		if(!visited[i]){
			result++;
			visited[i] = true;
			let q = [i];
			
			while(q.length > 0){
				const val = q.shift();
				for(const next of graph[val]){
					if(!visited[next]){
						visited[next] = true;
						q.push(next);
					}
				}
			}
		}
	}
	
	console.log(result);
});