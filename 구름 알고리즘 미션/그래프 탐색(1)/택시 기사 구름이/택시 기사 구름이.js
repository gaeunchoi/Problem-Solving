const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const [X, Y, Z] = input[1].split(" ").map(Number);
const goormMap = input.slice(2, 2 + N).map(line => line.split(" ").map(Number));
const customer = input.slice(2 + N).map(line => line.split(" ").map(Number));

const directions = [[-1, 0],[0, -1],[1, 0],[0, 1]];

const bfs = (start, end) => {
  const [sx, sy] = start;
  const [ex, ey] = end;
  const distance = Array.from({ length: N }, () => Array(N).fill(-1));
  const queue = [[sx, sy]];
  distance[sx][sy] = 0;

  while (queue.length > 0) {
    const [cx, cy] = queue.shift();

    for (const [dx, dy] of directions) {
      const nx = cx + dx;
      const ny = cy + dy;

      if (
        0 <= nx && nx < N &&
        0 <= ny && ny < N &&
        goormMap[nx][ny] !== 1 &&
        distance[nx][ny] === -1
      ) {
        distance[nx][ny] = distance[cx][cy] + 1;
        queue.push([nx, ny]);
      }
    }
  }

  return distance[ex][ey];
}

let [cy, cx] = [customer[0][1] - 1, customer[0][0] - 1];

let result = 0;
for (let i = 0; i < M; i++) {
  let [sy, sx, ey, ex] = customer[i].map(v => v - 1);
  
  let moveDis = 0;
  if (i !== 0) {
    moveDis = bfs([cx, cy], [sx, sy]);
  }
  const workDis = bfs([sx, sy], [ex, ey]);

  let charge = workDis <= 5 ? X : X + (workDis - 5) * Y;

  result += charge - (moveDis + workDis) * Z;

  [cy, cx] = [ey, ex];
}

console.log(result);
