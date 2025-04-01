function solution(s, n) {
  const lowerAlpha = 'abcdefghijklmnopqrstuvwxyz';
  const upperAlpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

  let result = '';
  [...s].forEach((ele) => {
    if(ele === ' ') result += ' ';
    else{
      if(ele === ele.toUpperCase()) result += upperAlpha[(upperAlpha.indexOf(ele) + n) % 26]
      else result += lowerAlpha[(lowerAlpha.indexOf(ele) + n) % 26]
    }})
  return result;
}

console.log(solution("z A Z", 2))
console.log(solution("a Z b c F", 2))