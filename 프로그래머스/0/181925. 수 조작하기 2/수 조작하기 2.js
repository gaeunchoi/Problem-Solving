function solution(numLog) {
  var answer = '';
  
  const order = {
    '1': 'w',
    '-1': 's',
    '10': 'd',
    '-10': 'a'
  };

  return numLog.slice(1).map((v, i) => order[v - numLog[i]]).join('')
}