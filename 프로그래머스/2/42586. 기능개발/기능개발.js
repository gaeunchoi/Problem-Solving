function solution(progresses, speeds) {
    let answer = [];
    let days = [];
    let front = 0;
    
    progresses.forEach((v, i) =>{
        days.push(Math.ceil((100 - v) / speeds[i]));
    })
    
    days.forEach((v, i) => {
        if(v > days[front]){
            answer.push(i - front);
            front = i;
        }
    })
    answer.push(days.length - front);
    
    return answer;
}