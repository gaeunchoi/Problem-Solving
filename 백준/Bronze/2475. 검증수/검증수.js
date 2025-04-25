const input = require("fs").readFileSync("/dev/stdin").toString().trim().split(" ").map(Number);
const sum = input.reduce((acc, num) => acc + num ** 2, 0);
console.log(sum % 10);