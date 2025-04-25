function solution(X, Y) {
    let countX = {}, countY = {};
    [...X].forEach(x => countX[x] = (countX[x] || 0) + 1);
    [...Y].forEach(y => countY[y] = (countY[y] || 0) + 1);

    let common = [];
    for(let i = 0 ; i <= 9 ; i++){
        const digit = i.toString();
        const digitCnt = Math.min(countX[digit] || 0, countY[digit] || 0);
        
        for(let j = 0 ; j < digitCnt ; j++){
            common.push(digit);
        }
    }
    
    if(common.length === 0) return "-1";
    
    const result = common.sort((a, b) => b - a).join("");
    return result[0] === "0" ? "0" : result;
}