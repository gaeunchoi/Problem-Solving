const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const input = [];
rl.on('line', (line) => input.push(line.trim())).on('close', () => {
  const [N, Q] = input[0].split(' ').map(Number);
  const X = input[1].split(' ').map(BigInt).sort((a, b) => (a < b ? -1 : 1)); // BigInt 비교

  for (let i = 2; i < 2 + Q; i++) {
    const p = BigInt(input[i]); // p도 BigInt로 받아야 함

    let left = 0;
    let right = N;

    // lower_bound 방식으로 p 이상인 가장 왼쪽 인덱스 찾기
    while (left < right) {
      const mid = Math.floor((left + right) / 2);
      if (X[mid] < p) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }

    const candidates = [];
    if (left > 0) candidates.push(X[left - 1]);
    if (left < N) candidates.push(X[left]);

    candidates.sort((a, b) => {
      const diffA = a > p ? a - p : p - a;
      const diffB = b > p ? b - p : p - b;

      if (diffA === diffB) return a < b ? -1 : 1;
      return diffA < diffB ? -1 : 1;
    });

    console.log(candidates[0].toString());
  }
});