const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);
const start = [];
const end = [];

const calcDistance = (x, y) => (x ** 2 + y ** 2) * 2;

for (let i = 1; i <= N; i++) {
  const [X, Y, T] = input[i].split(' ').map(Number);
  start.push(T);
  end.push(T + calcDistance(X, Y));
}

const events = [];
for (let i = 0; i < N; i++) {
  events.push([start[i], 1, i]);
  events.push([end[i], 0, i]);
}

events.sort((a, b) => a[0] - b[0] || a[1] - b[1]);

let cnt = 0;
let result = 0;
for (const [time, type, idx] of events) {
  if (type === 1) cnt++;
  else cnt--;
  result = Math.max(result, cnt);
}

let answer = 0;
for (let i = 0; i < N; i++) {
  answer += end[i] - start[i];
}

console.log(answer - result);
