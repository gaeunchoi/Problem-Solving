function solution(word) {
    const values = ['A', 'E', 'I', 'O', 'U'];
    let wordDict = [];
    
    function dfs(cur){
        wordDict.push(cur);
        if(cur.length === 5) return;
        
        for(let i = 0 ; i < 5 ; i++){
            dfs(cur + values[i]);
        }
        
    }
    
    dfs('');
    return (wordDict.indexOf(word));
}