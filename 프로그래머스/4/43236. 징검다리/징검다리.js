function solution(distance, rocks, n) {
  rocks.sort((a, b) => a-b);
  rocks.push(distance);

  let left = 1;
  let right = distance;
  let answer = 0;

  while(left <= right){
    let mid = Math.floor((left + right) / 2);

    let prev = 0;
    let removeCnt = 0;

    for(let rock of rocks){
      let gap = rock - prev;
      if (gap < mid) {  // 거리가 mid보다 작으면 제거!
        removeCnt++;  
      } else {  // mid보다 크거나 같으면 제거하지 않고 유지
        prev = rock;  // 이전 바위 위치를 갱신
      }
    }

    if(removeCnt > n){
      right = mid - 1;
    } else {
      answer = mid;
      left = mid + 1;
    }
  }
  return answer;
}