def solution(word):
    values = ['A', 'E', 'I', 'O', 'U']
    wordDict = []
    
    def dfs(cur):
        wordDict.append(cur)
        if len(cur) == 5: 
            return
        for i in range(5):
            dfs(cur + values[i])
        
    dfs('')
    return wordDict.index(word)