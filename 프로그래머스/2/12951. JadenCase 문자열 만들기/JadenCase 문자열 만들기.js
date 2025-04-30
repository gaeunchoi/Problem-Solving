function solution(s) {
    const splitWord = s.split(" ");
    
    result = [];
    for(let word of splitWord){
        if(word) result.push(word[0].toUpperCase() + word.slice(1).toLowerCase());
        else result.push("");
    }
    return result.join(" ");
}