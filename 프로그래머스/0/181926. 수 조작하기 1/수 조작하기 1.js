function solution(n, control) {
  var answer = n;
  
  const order = {
    'w': 1,
    's': -1,
    'd': 10,
    'a': -10
  };

  control.split('').forEach((value) => answer += order[value])
  return answer;
}