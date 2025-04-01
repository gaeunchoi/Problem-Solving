function solution(binomial) {
  [a, op, b] = binomial.split(" ");
  if(op === '+') return +a + +b
  else if(op === '-') return a-b
  else return a*b
}