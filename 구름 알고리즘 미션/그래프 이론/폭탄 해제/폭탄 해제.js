const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, M] = input[0].split(" ").map(Number);
const connectLine = [];
const connectCnt = Array(N).fill(0);

for(let i = 1 ; i <= M ; i++){
	const [A, B] = input[i].split(" ").map(Number);
	connectLine.push([A-1, B-1]);
	connectCnt[A-1]++; 
	connectCnt[B-1]++;
}

let result = [];
for(let i = 0 ; i < M ; i++){
	const [A, B] = connectLine[i];
	if(connectCnt[A] > 1 && connectCnt[B] > 1) {
		result.push(i+1);
	}
}

console.log(result.length > 0 ? result.join(" ") : -1);