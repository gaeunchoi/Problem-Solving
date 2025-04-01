function solution(k, m, score) {
  let sort = score.sort((a, b) => b - a);
  let answer = 0;
  let acc = 0;
  for (let i = m; i <= score.length; i += m) {
    let slice = sort.slice(acc, i);
    acc = i;
    answer += slice[slice.length - 1] * m;
  }
  return answer;
}