const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n');
const MOD = 1e9 + 7;

const [N, M, K] = input[0].split(' ').map(Number);

// 휴식: 1, 휴식 x: 0
const goormMap = Array.from({ length: N }, () => Array(M).fill(0));
for (let idx = 1; idx <= K; idx++) {
    const [r, c] = input[idx].split(' ').map(Number);
    goormMap[r - 1][c - 1] = 1;
}

const caseCnt = Array.from({ length: N }, () => Array(M).fill(0));
caseCnt[0][0] = 1;

const rowSum = Array.from({ length: N }, () => Array(M + 1).fill(0));
const colSum = Array.from({ length: N + 1 }, () => Array(M).fill(0));

for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
        if (goormMap[i][j]) {
            caseCnt[i][j] = 0;
        } else {
            if (i > 0) {
                let up = (colSum[i][j] - colSum[Math.max(0, i - 6)][j]) % MOD;
                if (up < 0) up += MOD;
                caseCnt[i][j] = (caseCnt[i][j] + up) % MOD;
            }
            if (j > 0) {
                let left = (rowSum[i][j] - rowSum[i][Math.max(0, j - 6)]) % MOD;
                if (left < 0) left += MOD;
                caseCnt[i][j] = (caseCnt[i][j] + left) % MOD;
            }
        }
        rowSum[i][j + 1] = (rowSum[i][j] + caseCnt[i][j]) % MOD;
        colSum[i + 1][j] = (colSum[i][j] + caseCnt[i][j]) % MOD;
    }
}

console.log(caseCnt[N - 1][M - 1]);
