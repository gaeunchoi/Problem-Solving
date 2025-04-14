function solution(n, costs) {
    const parent = new Array(n).fill(0).map((_, idx) => idx);
    
    function find(x){
        if(parent[x] === x) return x;
        return parent[x] = find(parent[x]);
    }
    
    function union(a, b) {
        const rootA = find(a);
        const rootB = find(b);
        
        if(rootA !== rootB) parent[rootB] = rootA;
    }
    
    costs.sort((a, b) => a[2] - b[2]);
    
    let result = 0;
    for(const [a, b, cost] of costs){
        if(find(a) !== find(b)){
            union(a, b);
            result += cost;
        }
    }
    return result;
}