function solution(n, left, right) {
    let nPowArr = [];
    for(let i = left ; i <= right ; i++){
        nPowArr.push(Math.max(Math.floor(i / n), i % n) + 1);
    }
    return(nPowArr);
}