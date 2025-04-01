function solution(arr, divisor) {
  let result = []
  arr.forEach(v => {
    if(v % divisor === 0) result.push(v)
  })
  return result.length ? result.sort((a, b) => a-b) : [-1]
}