function solution(n) {
  let v = Math.sqrt(n)
  return v === parseInt(v) ? (v+1)**2 : -1
}