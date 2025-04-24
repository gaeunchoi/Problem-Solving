function solution(N, stages) {
    const stagesCnt = new Map();
    for(const stage of stages){
        stagesCnt.set(stage, (stagesCnt.get(stage) || 0) + 1);
    }
    
    const result = [];
    const total = stages.length;
    let acc = 0;
    
    for(let i = 1 ; i <= N ; i++){
        const current = stagesCnt.get(i) || 0;
        const remaining = total - acc;
        const failRate = remaining === 0 ? 0 : current / remaining;
        acc += current;
        result.push([failRate, i]);
    }
    
    result.sort((a, b) => {
        if (b[0] === a[0]) {
            return a[1] - b[1]; // 실패율 같으면 스테이지 번호 낮은 순
        }
        return b[0] - a[0];
    });
    
    return result.map(item => item[1]);
}