// Run by Node.js
const readline = require('readline');

(async () => {
	let rl = readline.createInterface({ input: process.stdin });
	let input = [];
  let totalLines = 0;
	for await (const line of rl) {
    input.push(line);
    
		if (input.length === 2) { 
      const N = parseInt(input[1]);
      totalLines = 4 + N; // N + 4
    }

    if (totalLines && input.length === totalLines) {
        rl.close();
    }
	}
	
  // 방향 정의
  const directions = {'L': [-1, 0], 'R': [1, 0], 'U': [0, 1], 'D': [0, -1]};

  // 초기 위치
  let [x, y] = input[0].split(" ").map(Number);
  
  // 웅덩이 개수 + 웅덩이 좌표 받기
  const N = +input[1];
  let water = [];
  for(let i = 0 ; i < N ; i++){
    const [wx, wy] = input[2 + i].split(" ").map(Number);
    water.push([wx, wy]);
  }

  // 명령 개수 + 명령 받기
  const Q = +input[N+2];
  const orders = input[N+3].split(" ");


  orders.forEach(order => {
    const [dx, dy] = directions[order];
    const [mx, my] = [x + dx, y + dy];
    if(!water.some(([wx, wy]) => wx === mx && wy === my)) {
      [x, y] = [mx, my];
    }
  })

  console.log(x, y);
	process.exit();
})();
