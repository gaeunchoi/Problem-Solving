const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);
const tmp = input[1].split(' ').map(Number);

const taste = tmp.map((val, idx) => [val, idx]);

// 값 기준으로 오름차순 정렬
taste.sort((a, b) => a[0] - b[0]);

let valid = true;
for (let i = 0; i < N; i++) {
  if (taste[i][0] - i <= 0) {
    valid = false;
    break;
  }
}

if (!valid) {
  const result = Array.from({ length: N }, (_, i) => i + 1);
  console.log(result.join(' '));
} else {
  const result = taste.map(item => item[1] + 1);
  console.log(result.join(' '));
}
