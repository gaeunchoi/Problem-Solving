function findRemoveBlock(board){
    const removeArea = new Set();
    for(let i = 0 ; i < board.length - 1; i++){
        for(let j = 0 ; j < board[0].length - 1; j++){
            const cur = board[i][j];
            if (!cur) continue;
            if (cur === board[i][j + 1] && cur === board[i + 1][j] && cur === board[i + 1][j + 1]) {
                removeArea.add(`${i},${j}`);
                removeArea.add(`${i},${j + 1}`);
                removeArea.add(`${i + 1},${j}`);
                removeArea.add(`${i + 1},${j + 1}`);
            }
        }
    }
    return Array.from(removeArea).map(pos => pos.split(',').map(Number));
}

function removeBlock(board, positions){
    let cnt = 0;
    for(const [rx, ry] of positions){
        if(board[rx][ry]){
            board[rx][ry] = "";
            cnt++;
        }
    }
    return cnt;
}

function applyRemoveState(board){
    const row = board.length;
    const col = board[0].length;
    
    for (let j = 0; j < col; j++) {
        const stack = [];

        for (let i = row - 1; i >= 0; i--) {
            if (board[i][j] !== "") stack.push(board[i][j]);
        }

        for (let i = row - 1; i >= 0; i--) {
            board[i][j] = stack[row - 1 - i] || "";
        }
    }
}

function solution(m, n, board) {
    const arrBoard = board.map(row => row.split(""));
    let result = 0;
    
    while(true){
        const goRemove = findRemoveBlock(arrBoard);
        if(goRemove.length === 0) break;
        
        const removed = removeBlock(arrBoard, goRemove);
        result += removed;
        
        applyRemoveState(arrBoard);
    }
    
    return result;
}