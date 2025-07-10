function solution(n, wires) {
    let result = Number.MAX_SAFE_INTEGER
    let tree = Array.from(Array(n+1), () => [])
    wires.map(e => {
        let [a, b] = e
        tree[a].push(b)
        tree[b].push(a)
    })
    
    const bfs = (root, exceptNum) => {
        let cnt = 0
        let visited = []
        let q = [root]
        visited[root] = true
        
        while(q.length > 0){
            let idx = q.pop()
            tree[idx].forEach((element)=>{
                if(element !== exceptNum && !visited[element]){
                    visited[element] = true
                    q.push(element)
                }
            })
            cnt++
        }
        return cnt;
    }
    
    wires.forEach((wire) => {
        let [a, b] = wire
        result = Math.min(result, Math.abs(bfs(a, b) - bfs(b, a)))
    })
    
    return result
}