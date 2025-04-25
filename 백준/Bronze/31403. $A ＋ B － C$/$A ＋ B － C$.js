const input = require("fs").readFileSync('/dev/stdin').toString().trim().split("\n");

let A = input[0];
let B = input[1];
let C = input[2];

console.log(+A + +B - +C);
console.log(parseInt(A + B) - +C);