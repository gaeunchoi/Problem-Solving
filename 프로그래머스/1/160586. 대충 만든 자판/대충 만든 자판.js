function solution(keymap, targets) {
    let firstAppear = new Map();
    for(const mapping of keymap){
        [...mapping].forEach((v, idx) => {
            firstAppear.set(v, Math.min((firstAppear.get(v) || 100), idx+1));
        })
    }
    
    let result = [];
    for(const target of targets){
        cnt = 0;
        for(const t of target){
            if(!firstAppear.has(t)){
                cnt = -1;
                break;
            }
            cnt += firstAppear.get(t);
        }
        result.push(cnt);
    }
    return result;
}