function solution(n, arr1, arr2){
  let answer = [];
  const arrs = arr1.map((v, i) => [v, arr2[i]]);
  arrs.forEach(([i, j]) => {
    let row = (i|j).toString(2).padStart(n, 0);
    console.log(row);
    answer.push(row.replace(/1/gi, "#").replace(/0/gi, " "));
  })

  return answer;
}