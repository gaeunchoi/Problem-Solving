function solution(priorities, location) {
    var answer = 0;
    let queue = priorities.map((v, i) => [v, i]);
    
    while(queue){
        let popElement = queue.shift();
        if(queue.some(v => v[0] > popElement[0])){
            queue.push(popElement);
        } else {
            answer++;
            if(popElement[1] === location) return answer;
        }
    }
    return answer;
}