const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	
	for await (const line of rl) {
		input.push(line);
		if(input.length === input[0]+1) rl.close();
	}
	
	const N = input[0];
	let [minP, maxP] = [100000, 0];
	let [minN, maxN] = ["", ""];
	
	for(let i = 1 ; i <= N ; i++){
		let [S, P] = input[i].split(" ")
		if(maxP < +P){
			maxP = +P;
			maxN = S;
		}
		if(minP > +P){
			minP = +P;
			minN = S;
		}
	}
	
	console.log(maxN, maxP);
	console.log(minN, minP);
	
	process.exit();
})();
