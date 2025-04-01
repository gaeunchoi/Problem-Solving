// 참여 안하는사람 거르고 점수순으로 정렬
function solution(rank, attendance) {
  var answer = [];
  rank.forEach((score, i) => {
    if(attendance[i]) answer.push([score, i]) 
  })

  answer.sort((a, b) => {
    if(a[0] > b[0]) return 1;
    if(a[0] < b[0]) return -1
  })

  return 10000*answer[0][1] + 100*answer[1][1] + answer[2][1];
}