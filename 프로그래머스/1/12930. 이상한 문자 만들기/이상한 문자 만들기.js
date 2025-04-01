function solution(s) {
  var answer = '';

  let i = 0;
  [...s].forEach((v) => {
    if(v === ' '){
      answer += ' '
      i = 0;
    } else {
      answer += (i++)%2 === 0 ? v.toUpperCase() : v.toLowerCase();
    }
  })
  return answer;
}