function solution(num) {
  var answer = 0;
  while(num !== 1){
    num = num % 2 === 0 ? num/2 : 3*num +1
    answer++;
  }
  return answer < 500 ? answer : -1;
}