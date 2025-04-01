function solution(arr, queries) {
  let answer = []
  queries.map(([s, e, k]) => {
    const filteredArr = arr.slice(s, e+1).filter(v => v > k)
    answer.push(filteredArr.length ? Math.min(...filteredArr) : -1)
  });
  return answer
}