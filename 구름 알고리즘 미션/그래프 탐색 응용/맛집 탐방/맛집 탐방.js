const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = parseInt(input[0]);
const graph = Array.from({ length: N + 1 }, () => []);

for (let i = 1; i < N; i++) {
  const [u, v] = input[i].split(" ").map(Number);
  graph[u].push(v);
  graph[v].push(u);
}

function dfs(start) {
  const visited = Array(N + 1).fill(false);
  const stack = [[start, 0]];
  let farNode = start;
  let maxDist = 0;

  while (stack.length > 0) {
    const [node, dist] = stack.pop();

    if (visited[node]) continue;
    visited[node] = true;

    if (dist > maxDist) {
      maxDist = dist;
      farNode = node;
    }

    for (const next of graph[node]) {
      if (!visited[next]) {
        stack.push([next, dist + 1]);
      }
    }
  }

  return [farNode, maxDist];
}

const [nodeA] = dfs(1);
const [, diameter] = dfs(nodeA);

console.log(diameter + 1);
