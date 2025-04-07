// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	
	for await (const line of rl) {
		let [W, R] = line.split(" ");
		console.log(parseInt(+W * (1 + R/30)));
		rl.close();
	}
	
	process.exit();
})();
