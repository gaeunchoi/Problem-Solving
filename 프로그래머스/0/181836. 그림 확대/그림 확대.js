function solution(picture, k) {
  var answer = [];
  picture.forEach(row => {
    let tmp = '';
    for(let pixel of row){
      tmp += pixel.repeat(k)
    }
    for(let i = 0 ; i < k ; i++){
      answer.push(tmp)
    }
  })
  return answer;
}