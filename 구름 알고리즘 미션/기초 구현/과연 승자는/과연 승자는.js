// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];

	for await (const line of rl) {
    input.push(line);
    if(input.length === 3) rl.close();
	}
	
  const N = +input[0];
  const Alice = input[1].split(" ").map(v => +v);
  const Bob = input[2].split(" ").map(v => +v);
  let [scoreA, scoreB] = [0, 0];

  for(let i = 0 ; i < N ; i++){
    if(Alice[i] === Bob[i]){
      scoreA++; 
      scoreB++;
    } else if(Alice[i] < Bob[i]) {
      if(Bob[i] - Alice[i] === 7){
        scoreA += 3;
        scoreB--;
      } else {
        scoreB += 2;
      }
    } else {
      if(Alice[i] - Bob[i] === 7){
        scoreA--;
        scoreB += 3;
      } else {
        scoreA += 2;
      }
    }
  }

  console.log(scoreA, scoreB);
	process.exit();
})();
