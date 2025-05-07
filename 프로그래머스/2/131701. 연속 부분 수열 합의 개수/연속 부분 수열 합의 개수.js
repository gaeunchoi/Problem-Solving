function solution(elements) {
    const N = elements.length;
    const circleElement = elements.concat(elements);
    let result = new Set();
    
    for(let len = 1 ; len <= N ; len++){
        for(let s = 0 ; s < N ; s++){
            result.add(circleElement.slice(s, s + len).reduce((acc, cur) => acc + cur, 0));
        }
    }
    
    return result.size;
}