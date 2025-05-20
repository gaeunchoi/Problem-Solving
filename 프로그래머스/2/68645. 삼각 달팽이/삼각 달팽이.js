function solution(n) {
  const arr = Array.from({ length: n }, (_, i) => Array(i + 1).fill(0));
  const directions = [
    [1, 0],   // 아래
    [0, 1],   // 오른쪽
    [-1, -1], // 왼쪽위 (좌측 대각선 위)
  ];

  let turn = 0;
  let x = 0, y = 0;
  let i = 1;
  const endNum = (n * (n + 1)) / 2;

  while (i <= endNum) {
    arr[x][y] = i++;
    const [dx, dy] = directions[turn];
    const mx = x + dx;
    const my = y + dy;

    if (mx >= 0 && mx < n && my >= 0 && my <= mx && arr[mx][my] === 0) {
      x = mx;
      y = my;
    } else {
      turn = (turn + 1) % 3;
      x += directions[turn][0];
      y += directions[turn][1];
    }
  }

  const answer = [];
  for (const row of arr) {
    for (const num of row) {
      answer.push(num);
    }
  }

  return answer;
}
