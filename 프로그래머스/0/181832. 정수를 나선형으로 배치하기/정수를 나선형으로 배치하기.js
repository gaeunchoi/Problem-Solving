function solution(n) {
  const directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  let answer = Array.from(new Array(n), () => new Array(n).fill(0))

  let [x, y] = [0, 0]
  let d = 0

  for(let i = 1 ; i <= n**2; i++){
    answer[x][y] = i;
    let [mx, my] = [x + directions[d][0], y + directions[d][1]]
    
    if(0 <= mx && mx < n && 0 <= my && my < n && answer[mx][my] === 0 ){
      [x, y] = [mx, my];
    } else {
      d = (d+1) % 4;
      [x, y] = [x + directions[d][0], y + directions[d][1]];
    }
  }
  return answer;
}