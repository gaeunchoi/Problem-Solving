function solution(board, moves) {
    const N = board.length
    let topIdx = Array(N).fill(-1);
    for(let i = 0 ; i < N ; i++){
        for(let j = 0 ; j < N ; j++){
            if(topIdx[j] === -1 && board[i][j] !== 0) topIdx[j] = i;
        }
    }
    
    let result = 0;
    let stack = [];
    moves.forEach((move) => {
        const curIdx = topIdx[move-1];
        if(curIdx !== -1 && curIdx < N){
            if(stack[stack.length-1] === board[curIdx][move-1]){
                result += 2;
                stack.pop();
            } else {
                stack.push(board[curIdx][move-1]);
            }
            topIdx[move-1] = curIdx + 1;
        }
    })
    return(result);
}