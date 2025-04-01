function solution(number) {
  const getCombination = (arr, n) => {
    if(n === 1) return arr.map(v => [v]);

    const result = [];
    arr.forEach((fixed, idx, origin) => {
      const rest = origin.slice(idx+1)
      const combis = getCombination(rest, n-1);
      const attached = combis.map(combi => [fixed, ...combi]);
      result.push(...attached);
    })

    return result;
  }
  
  let answer = 0
  const combiNum = getCombination(number, 3)
  combiNum.forEach((ele) => {
    const sum = ele.reduce((acc, val) => acc+val, 0)
    answer += sum === 0 ? 1 : 0
  })
  return answer;
}