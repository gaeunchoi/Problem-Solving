// Run by Node.js
const readline = require('readline');

(async () => {
    let rl = readline.createInterface({ input: process.stdin });
    let input = [];
    for await (const line of rl) {
        input.push(line);
        if (input.length === 3) rl.close();
    }

    const N = +input[0];
    const A = input[1].split(" ").map(Number).sort((a, b) => a - b); // 작은 값부터 탐색
    const K = +input[2];
    
    let result = Infinity;

    function findResult(cur) {
				let num = cur.length > 0 ? +cur : 0;
				if (cur.length > 0 && cur[0] === '0') return;
				if (cur.length > String(K).length + 1) return;
			
        // 현재 숫자가 K보다 크다면 결과 갱신
        if (num > K) {
            result = Math.min(result, num);
            return;
        }

        for (let digit of A) {
            findResult(cur + digit);
        }
    }

    findResult("");
    console.log(result);
    process.exit();
})();
