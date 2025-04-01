// Testcase 16번만 못뚫었음 ㅇㅅㅇ ...
// reportInfo에는 key(본인)을 신고한 사람의 리스트 저장
// result에는 내가 신고한사람이 몇명 정지당했는지 저장
function solution(id_list, report, k){
  let reportInfo = {};
  let result = {};
  id_list.forEach(userId => {
    reportInfo[userId] = [];
    result[userId] = 0;
  });

  new Set(report).forEach((reportStr) => {
    let [userId, targetId] = reportStr.split(" ");

    if(!(reportInfo[targetId].includes(userId))) reportInfo[targetId].push(userId);
  });

  Object.entries(reportInfo).forEach(([_, reporters]) => {
    if(reporters.length >= k){
      reporters.forEach(user => result[user]++);
    }
  })

  return Object.values(result);
}