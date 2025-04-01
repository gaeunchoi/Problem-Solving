function solution(left, right) {
  var answer = 0;
  for(let i = left ; i <= right ; i++){
    answer += parseInt(i**0.5) === i**0.5 ? -i : i
  }
  return answer;
}