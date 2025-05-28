function solution(queue1, queue2) {
    const arr = [...queue1, ...queue2];
    const n = queue1.length;
    
    const q1 = [...queue1];
    const q2 = [...queue2];
    
    let sum1 = q1.reduce((acc, cur) => acc + cur, 0);
    let sum2 = q2.reduce((acc, cur) => acc + cur, 0);
    const total = sum1 + sum2;
    
    if(total % 2 !== 0) return -1;
    const target = total / 2;
    
    let p1 = 0;
    let p2 = n;
    
    let cnt = 0;
    const maxCnt = queue1.length * 3;
    
    while(cnt <= maxCnt){
        if(sum1 === target) return cnt;
        
        if(sum1 > target){
            sum1 -= arr[p1];
            sum2 += arr[p1];
            p1++;
        } else {
            sum2 -= arr[p2];
            sum1 += arr[p2];
            p2++;
        }
        cnt++;
    }
    
    return -1;
}