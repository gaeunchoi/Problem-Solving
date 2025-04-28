function solution(numbers, hand) {
    const left = [1, 4, 7], right = [3, 6, 9];
    let leftPos = [3, 0], rightPos = [3, 2];
    let answer = [];

    const addLeft = (curRow, col) => {
        answer.push('L');
        leftPos = [curRow, col];
    }
    
    const addRight = (curRow, col) => {
        answer.push('R');
        rightPos = [curRow, col];
    }
    
    numbers.forEach(number => {
        const [row, col] = number === 0 ? [3, 1] : [(number - 1) / 3 >> 0, (number - 1) % 3];
        if(left.includes(number)) {
            addLeft(row, col);
        }
        else if(right.includes(number)) {
            addRight(row, col);
        } else {
            const leftDis = Math.abs(leftPos[0] - row) + Math.abs(leftPos[1] - col);
            const rightDis = Math.abs(rightPos[0] - row) + Math.abs(rightPos[1] - col);
            
            if(leftDis < rightDis) {
                addLeft(row, col);
            } else if (rightDis < leftDis) {
                addRight(row, col);
            } else {
                if(hand === 'left') {
                    addLeft(row, col);
                } else {
                    addRight(row, col);
                }
            }
        }
    })
    
    return answer.join("");
}