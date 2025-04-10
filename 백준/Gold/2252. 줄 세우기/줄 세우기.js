const file = process.platform === 'linux' ? 0 : './input.txt';
const input = require("fs").readFileSync(file).toString().split("\n");

const [N, M] = input[0].split(" ").map(Number);
let comparisons = [];
for(let i = 1 ; i <= M ; i++){
    const [A, B] = input[i].split(" ").map(Number);
    comparisons.push([A, B]);
}

const topologySort = (n, comparisons) => {
    const graph = Array.from({length: n+1}, () => []);
    const indegree = Array(n+1).fill(0);

    for(const [a, b] of comparisons){
        graph[a].push(b);
        indegree[b] += 1;
    }

    const q = [];
    const result = [];

    for(let i = 1 ; i <= n ; i ++){
        if(indegree[i] === 0) q.push(i);
    }

    while(q.length > 0){
        const current = q.shift();
        result.push(current);

        for(const next of graph[current]){
            indegree[next] -= 1;
            if(indegree[next] === 0) q.push(next);
        }
    }
    return result;
}

console.log(topologySort(N, comparisons).join(" "));