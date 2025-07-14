function solution(players, m, k) {
    let result = 0;
    let servers = Array(24).fill(0)
    
    players.forEach((player, idx) => {
        if(parseInt(player / m) > servers[idx]){
            let addServerCnt = parseInt(player / m) - servers[idx]
            
            for(let i = 0 ; i < k ; ++i){
                if(idx + 1 <= 23) servers[idx+i] = servers[idx+i] + addServerCnt
            }
            result += addServerCnt;
        }
    })
    return result
}