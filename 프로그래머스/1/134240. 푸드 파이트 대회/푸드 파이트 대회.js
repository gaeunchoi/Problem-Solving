function solution(food) {
  let left = '';
  food.forEach((count, i) => {
    if (i > 0) {
      left += String(i).repeat(Math.floor(count / 2));
    }
  });

  return left + '0' + [...left].reverse().join('');
}