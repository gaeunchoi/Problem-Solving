function solution(name) {
    let charMove = 0;
    let cursorMove = name.length - 1;
    const ordA = 'A'.charCodeAt();
    const ordZ = 'Z'.charCodeAt();
    
    [...name].forEach((val, i) => {
        const ordVal = val.charCodeAt();
        charMove += Math.min(ordVal - ordA, ordZ - ordVal + 1);
        
        let next = i + 1;
        while(next < name.length && name[next] === 'A') next++;
        
        cursorMove = Math.min(cursorMove, 2*i + name.length - next, i + 2 * (name.length - next))
    })
    
    return charMove + cursorMove;
}