function solution(num_list) {
  let odd = 0, even = 0;

  num_list.forEach((x, i) => i % 2 === 0 ? even += x : odd += x);
  return Math.max(odd, even);
}