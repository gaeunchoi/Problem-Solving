function solution(records) {
    let result = [];
    let matchIdName = {};
    
    for(const record of records){
        const splitRecord = record.split(" ");
        const action = splitRecord[0];
        const userId = splitRecord[1];
        
        if(["Enter", "Change"].includes(action)){
            const userName = splitRecord[2];
            matchIdName[userId] = userName;
        }
        
        if(action === "Enter"){
            result.push([userId, "IN"]);
        } else if(action === "Leave"){
            result.push([userId, "OUT"]);
        }
    }
    
    let answer = [];
    for(const [uId, status] of result){
        const uName = matchIdName[uId];
        answer.push(status === "IN" ? `${uName}님이 들어왔습니다.` : `${uName}님이 나갔습니다.`);
    }
    return answer;
}