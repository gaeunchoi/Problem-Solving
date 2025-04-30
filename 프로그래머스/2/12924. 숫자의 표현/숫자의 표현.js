function solution(num) {
  let result = 0;
  for (var i = 1; i <= num; i++) {
    if (num % i == 0 && i % 2 == 1) result++;
  }
  return result;
}