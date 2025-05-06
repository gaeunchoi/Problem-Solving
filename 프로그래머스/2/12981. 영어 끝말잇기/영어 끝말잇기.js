function solution(n, words) {
    let wordRelay = [words[0]];
    
    for(let i = 1 ; i < words.length ; i++){
        const prevWord = wordRelay[wordRelay.length - 1];
        const currWord = words[i];
        
        if(wordRelay.includes(currWord) || prevWord[prevWord.length - 1] !== currWord[0] || currWord.length === 1){
            return [(i % n) + 1, Math.floor(i / n) + 1];
        }
        wordRelay.push(currWord);
    }
    return [0, 0];
}