function solution(l, r) {
  var answer = [];
  for(let i = l ; i <= r ; i++){
    if([...String(i)].every(n => n === '0' || n ==='5')) answer.push(i)
  }
  return answer.length > 0 ? answer : [-1];
}