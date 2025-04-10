// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
	for await (const line of rl) {
		input.push(line);
		if(input.length === input[0] + 1) rl.close();
	}
	
	const N = +input[0];
	let store = {};
	for(let i = 1 ; i <= N ; i++){
		const [S, A] = input[i].split(" ");
		if(!(S in store)){
			store[S] = +A;
		} else {
			store[S] += +A;
		}
	}
	
	const result = Object.keys(store).sort().reduce((newObj, key) => {
		newObj[key] = store[key];
		return newObj;
	}, {});
	
	for(const key in result){
		console.log(key, result[key]);
	}
	process.exit();
})();
