function solution(k, score) {
    let answer = [];
    let honor = [];
    for(let i = 0 ; i < score.length ; i++){
        if(honor.length < k) honor.push(score[i]);
        else {
            let min = Math.min(...honor)
            if(score[i] > min){
                honor.pop(min);
                honor.push(+score[i]);
            }
        }
        honor.sort((a, b) => b-a);
        answer.push(+(honor.slice(-1)))
    }
    return answer;
}