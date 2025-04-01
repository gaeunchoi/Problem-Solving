function solution(n) {
  let answer = ''
  while(n != 0){
    answer += n % 3
    n = parseInt(n/3)
  }
  return parseInt(answer, 3)
}