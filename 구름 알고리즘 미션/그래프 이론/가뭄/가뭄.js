const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let idx = 0;
const T = Number(input[idx++]);

for (let t = 0; t < T; t++) {
  const [N, M] = input[idx++].split(" ").map(Number);
  const waterload = [];

  for (let i = 0; i < M; i++) {
    waterload.push(input[idx++].split(" ").map(Number));
  }

  console.log(N - 1);
}