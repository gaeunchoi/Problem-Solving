const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	
	for await (const line of rl) {
		input.push(line);
		if(input.length === input[0]+1) rl.close();
	}
	
	const T = input[0];
	let result = 0;
	
	for(let i = 1 ; i <= T ; i++){
		const [a, op, b] = input[i].split(" ");
		switch(op){
			case '+':
				result += +a + +b;
				break;
			case '-':
				result += +a - +b;
				break;
			case '*':
				result += +a * +b;
				break;
			case '/':
				result += Math.floor(+a / +b);
				break;
		}
	}
	console.log(result);
	process.exit();
})();
