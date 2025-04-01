function solution(intStrs, k, s, l) {
  return intStrs.map((v) => [...v.slice(s, s+l)].join('')).filter(e => e > k).map(a => +a)
}