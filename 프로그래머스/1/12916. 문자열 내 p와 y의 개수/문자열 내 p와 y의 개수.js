function solution(s){
  let [cntP, cntY] = [0, 0];

  [...s].forEach(ele => {
    if(ele === 'p' || ele === 'P') cntP++
    if(ele === 'y' || ele === 'Y') cntY++
  })
  return cntP === cntY ? true : false;
}