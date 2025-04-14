const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let [A, B, C] = input[0].split(' ').map(Number);
const N = +input[1];
const chargers = input.slice(2).map(line => {
  const [price, type] = line.split(' ').map(Number);
  return { price, type };
});

chargers.sort((a, b) => a.price - b.price);

let count = 0;
let total = 0;

for (const charger of chargers) {
  const { price, type } = charger;

  if (type === 0) { // X 타입
    if (A > 0) {
      A--;
    } else if (C > 0) {
      C--;
    } else {
      continue;
    }
  } else { // Y 타입
    if (B > 0) {
      B--;
    } else if (C > 0) {
      C--;
    } else {
      continue;
    }
  }

  count++;
  total += price;
}

console.log(count, total);
