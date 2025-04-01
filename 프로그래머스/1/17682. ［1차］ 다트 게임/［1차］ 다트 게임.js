function solution(dartResult) {
  let score = '';
  let result = [];
  [...dartResult].forEach(dart => {
    if(dart === 'S'){
      result.push(parseInt(score))
      score = ''
    } else if(dart === 'D'){
      result.push(parseInt(score) ** 2);
      score = ''
    } else if(dart === 'T'){
      result.push(parseInt(score) ** 3);
      score = ''
    } else if(dart === '*'){
      const lenResult = result.length
      if(lenResult <= 1) {
        result[0] *= 2;
      } else {
        result[lenResult-2] *= 2;
        result[lenResult-1] *= 2;
      }
    } else if(dart === '#'){
      result[result.length-1] *= -1;
    } else {
      score += dart;
    }
  })

  return result.reduce((acc, cur) => acc + cur, 0);
}