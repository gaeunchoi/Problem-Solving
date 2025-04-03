function solution(cards1, cards2, goal) {
    var answer = [];
    let idx1 = 0, idx2 = 0;
    for(let i = 0 ; i < goal.length ; i++){
        if(idx1 < cards1.length && goal[i] === cards1[idx1]) answer.push(cards1[idx1++]);
        else if(idx2 < cards2.length && goal[i] === cards2[idx2]) answer.push(cards2[idx2++]);
        else break;
    }
    return JSON.stringify(goal) === JSON.stringify(answer) ? "Yes" : "No";
}